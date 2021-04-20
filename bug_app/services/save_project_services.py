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

def save_project_services(request):
    result = {}
    logger.debug('**********************************************************************')
    logger.debug("bug_app_save_project_services")
    name        = request.POST['name']
    id_users    = request.POST.getlist('id_users[]')
    logger.debug(name)
    logger.debug(id_users)
    # process to create username
    ## access property of instances use _ if you need to pass instance just pass it like an object
    user = User.objects.filter(id__in=id_users)
    # project = Projects.objects.create(name=name)
    # project.id_users.set(user)
    # project.save()
    #
    obj,created = Projects.objects.update_or_create(name=name,defaults={'name':name,},)
    obj.id_users.set(user)
    ##33
    success = True
    result['success'] = success
    return HttpResponse(json.dumps(result), content_type="application/json")


