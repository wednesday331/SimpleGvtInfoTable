#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
The main file for executing Python code
for the Government Table Project.
"""


import io
import json
import pandas as pd
import requests

from collections import OrderedDict
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from pandas.io.json import json_normalize

def index (request):
    """
    The following code requests a JSON response and
    converts it into a sortable table.
    """
    if request.method == 'POST' and 'fetch_data' in request.POST:
        #Makes the request
        response = requests.get("https://api.usaspending.gov/api/v2/references/toptier_agencies/")
        json_data = json.loads(response.text)
        df = pd.DataFrame(json_normalize(json_data['results']))
        html = df.to_html()
        return render(request, "mock/index.html",
                      {"table_stuff":html}
                     )
    if request.method == 'GET':
        response = requests.get("https://api.usaspending.gov/api/v2/references/toptier_agencies/")
        json_data = json.loads(response.text)
        df = pd.DataFrame(json_normalize(json_data['results']))
        answer = request.GET.get('sorting_arrangement','')
        if answer== 'select':
            df = pd.DataFrame(json_normalize(json_data['results']))
            html = df.to_html()
            return render(request, "mock/index.html",
                          {"table_stuff":html})
        if answer== 'agency_idascending':
            df.sort_values(by=['agency_id'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html",
                          {"table_stuff":html})
        if answer== 'toptier_code_ascending':
            df.sort_values(by=['toptier_code'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'abbreviation_ascending':
            df.sort_values(by=['abbreviation'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'agency_name_ascending':
            df.sort_values(by=['agency_name'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'congressional_justification_url_ascending':
            df.sort_values(by=['congressional_justification_url'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'active_fy_ascending':
            df.sort_values(by=['active_fy'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'active_fq_ascending':
            df.sort_values(by=['active_fq'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'outlay_amount_ascending':
            df.sort_values(by=['outlay_amount'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'obligated_amount_ascending':
            df.sort_values(by=['obligated_amount'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'budget_authority_amount_ascending':
            df.sort_values(by=['budget_authority_amount'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'current_total_budget_authority_amount_ascending':
            df.sort_values(by=['current_total_budget_authority_amount'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'percentage_of_total_budget_authority_ascending':
            df.sort_values(by=['percentage_of_total_budget_authority'], inplace=True)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'agency_id_descending':
            df.sort_values(by=['agency_id'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'toptier_code_descending':
            df.sort_values(by=['toptier_code'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'abbreviation_descending':
            df.sort_values(by=['abbreviation'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'agency_name_descending':
            df.sort_values(by=['agency_name'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'congressional_justification_url_descending':
            df.sort_values(by=['congressional_justification_url'],
                           inplace=True,
                           ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'active_fy_descending':
            df.sort_values(by=['active_fy'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'active_fq_descending':
            df.sort_values(by=['active_fq'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'outlay_amount_descending':
            df.sort_values(by=['outlay_amount'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'obligated_amount_descending':
            df.sort_values(by=['obligated_amount'], inplace=True, ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'budget_authority_amount_descending':
            df.sort_values(by=['budget_authority_amount'],
                           inplace=True,
                           ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'current_total_budget_authority_amount_descending':
            df.sort_values(by=['current_total_budget_authority_amount'],
                           inplace=True, 
                           ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        if answer== 'percentage_of_total_budget_authority_descending':
            df.sort_values(by=['percentage_of_total_budget_authority'],
                           inplace=True,
                           ascending=False)
            html = df.to_html()
            return render(request, "mock/index.html", {"table_stuff":html})
        else:
            return render(request, "mock/index.html")
    return render(request, "mock/index.html")
