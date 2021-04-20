# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from bug_app.models import *
import json, datetime
from datetime import datetime
import uuid
# Log
import logging
logger = logging.getLogger(__name__)

def create_ticket_services(request):
    result = {}
    logger.debug('**********************************************************************')
    logger.debug("bug_app_create_ticket_services")
    # id_users    = request.POST.getlist('id_users[]')
    project_id       = request.POST['project_id']
    name             = request.POST['name']
    description      = request.POST['description']
    id_priority      = request.POST['id_priority']
    id_status        = request.POST['id_status']
    id_typeticket    = request.POST['id_typeticket']
    id_reporter      = request.POST['id_reporter']
    id_assignedto    = request.POST['id_assignedto']
    version_reported = request.POST['id_version_reported']
    fixed_version    = request.POST['id_fixed_version']
    # process to create username
    ## access property of instances use _ if you need to pass instance just pass it like an object
    user_reporter   = User.objects.get(id=id_reporter)
    user_assignedto = User.objects.get(id=id_assignedto)
    project         = Projects.objects.get(id=project_id)
    # project.save()
    #
    obj,created = Tickets.objects.update_or_create(name=name,defaults={
        'name':name,'description':description,'priority':id_priority,
        'status':id_status,'typeticket':id_typeticket,
        'version_reported':version_reported,'fixed_version':fixed_version,
        'reporter':user_reporter,'assignedto':user_assignedto,'project_id':project,
        },)
    # obj.reporter.set(user_reporter)
    # obj.assignedto.set(user_assignedto)
    # obj.project_id.set(project)
    # obj.save()
    ##33
    success = True
    result['success'] = success
    return HttpResponse(json.dumps(result), content_type="application/json")


