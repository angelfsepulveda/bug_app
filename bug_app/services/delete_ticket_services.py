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

def delete_ticket_services(request):
    result = {}
    logger.debug('**********************************************************************')
    logger.debug("delete_ticket_services")
    id_ticket        = request.POST['id_ticket']
    #
    Tickets.objects.filter(id=id_ticket).delete()
    ##33
    success = True
    result['success'] = success
    return HttpResponse(json.dumps(result), content_type="application/json")


