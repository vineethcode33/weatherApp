# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import json

# Create your views here.
def index(request):
	resp_obj = {}
	with open('icons.json') as icons:
		icons_json = json.load(icons)
	api_key = '1f4fc2b3dc16281ffb6b17bb6c3f20a5'


	# {"api_key":'1f4fc2b3dc16281ffb6b17bb6c3f20a5',"icons_json": icons_json}

	return render_to_response("forecast/base.html",{"api_key":api_key,
		"icons":icons_json})