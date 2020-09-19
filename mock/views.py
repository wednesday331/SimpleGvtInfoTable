from django.shortcuts import render
import io
# Create your views here.
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
import pandas as pd
import requests
import json
from collections import OrderedDict
from pandas.io.json import json_normalize





def index (request):
    if request.method == 'POST' and 'fetchdata' in request.POST:
        #Makes the request
        response = requests.get("https://api.usaspending.gov/api/v2/references/toptier_agencies/")
        json_data = json.loads(response.text)
        df = pd.DataFrame(json_normalize(json_data['results']))
        html = df.to_html()
        return render(request, "mock/index.html", {"tablestuff":html})

    if request.method == 'GET':
        response = requests.get("https://api.usaspending.gov/api/v2/references/toptier_agencies/")
        json_data = json.loads(response.text)
        df = pd.DataFrame(json_normalize(json_data['results']))
        answer = request.GET.get('sortingarrangement','')
        if answer== '':
            df = pd.DataFrame(json_normalize(json_data['results']))
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})
        if answer== 'agency_idascending':
            df.sort_values(by=['agency_id'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'toptier_codeascending':
            df.sort_values(by=['toptier_code'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'abbreviationascending':
            df.sort_values(by=['abbreviation'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'agency_nameascending':
            df.sort_values(by=['agency_name'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'congressional_justification_urlascending':
            df.sort_values(by=['congressional_justification_url'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'active_fyascending':
            df.sort_values(by=['active_fy'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'active_fqascending':
            df.sort_values(by=['active_fq'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'outlay_amountascending':
            df.sort_values(by=['outlay_amount'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'obligated_amountascending':
            df.sort_values(by=['obligated_amount'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'budget_authority_amountascending':
            df.sort_values(by=['budget_authority_amount'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'current_total_budget_authority_amountascending':
            df.sort_values(by=['current_total_budget_authority_amount'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'percentage_of_total_budget_authorityascending':
            df.sort_values(by=['percentage_of_total_budget_authority'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'agency_iddescending':
            df.sort_values(by=['agency_id'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'toptier_codedescending':
            df.sort_values(by=['toptier_code'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'abbreviationdescending':
            df.sort_values(by=['abbreviation'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'agency_namedescending':
            df.sort_values(by=['agency_name'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'congressional_justification_urldescending':
            df.sort_values(by=['congressional_justification_url'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'active_fydescending':
            df.sort_values(by=['active_fy'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'active_fqdescending':
            df.sort_values(by=['active_fq'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'outlay_amountdescending':
            df.sort_values(by=['outlay_amount'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'obligated_amountdescending':
            df.sort_values(by=['obligated_amount'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'budget_authority_amountdescending':
            df.sort_values(by=['budget_authority_amount'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'current_total_budget_authority_amountdescending':
            df.sort_values(by=['current_total_budget_authority_amount'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

        if answer== 'percentage_of_total_budget_authoritydescending':
            df.sort_values(by=['percentage_of_total_budget_authority'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"tablestuff":html})

    return render(request, "mock/index.html")
