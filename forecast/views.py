# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
	return render_to_response("forecast/base.html")