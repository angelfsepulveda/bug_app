# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
# from openpyxl import *
# from openpyxl import load_workbook
from bug_app.models import *
import json, datetime
from datetime import datetime
import uuid
# Log
import logging
logger = logging.getLogger(__name__)

def register_services(request):
    result = {}
    logger.debug('**********************************************************************')
    logger.debug("bug_app_register_services")
    password    = request.POST['password']
    first_name  = request.POST['first_name']
    last_name   = request.POST['last_name']
    email       = request.POST['email']
    rol       = request.POST['rol']
    # process to create username
    first_name_split = first_name.split()
    last_name_split  = last_name.split()
    for x,y in enumerate(first_name_split):
        if x == 0:
            username = y[0:1]
    for x,y in enumerate(last_name_split):
        if x == 0:
            username = username+y
    
    logger.debug(username)
    ## access property of instances use _ if you need to pass instance just pass it like an object
    user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
    user.set_password(password)
    Users_info.objects.create(id_user=user,role=rol)
    user.save()
    ##33
    success = True
    result['success'] = success
    return HttpResponse(json.dumps(result), content_type="application/json")


