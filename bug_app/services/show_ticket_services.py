# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from bug_app.models import *
from django.db.models import Q
import json
# Log
import logging
logger = logging.getLogger(__name__)

def show_ticket_services(request):
    context = {}
    logger.debug("show_ticket_services")
    # archivo_excel          = request.POST['archivo_excel']
    # logger.debug(fecha_quarter)
        # fechacompra = r.fechacompra.strftime('%d/%m/%Y')
     # fechaexpira = r.fechaexpira.strftime('%d/%m/%Y')
    # archivos_database.setdefault(r.id,{'nombre':r.nombre,'cantidad':r.cantidad,'preciocompra':r.preciocompra,'ganancia':r.ganancia,'fechacompra':fechacompra,'fechaexpira':fechaexpira,'categoria':r.categoria,'perdido':r.perdido})
    archivos_database = {}
    for r in Tickets.objects.all():
        date_submitted = r.date_submitted.strftime('%d/%m/%Y')
        archivos_database.setdefault(r.id,{
            'name':r.name,'description':r.description,'priority':priority_choices[int(r.priority)][1],'status':status_choices[int(r.status)][1],
            'typeticket':type_choices[int(r.typeticket)][1],'reporter':r.reporter.username,'assignedto':r.assignedto.username,'version_reported':r.version_reported,
            'fixed_version':r.fixed_version,'date_submitted':date_submitted,'project_name':r.project_id.name,'id_project':r.project_id.id,
            'id_priority':r.priority,'id_status':r.status,'id_typeticket':r.typeticket,'id_reporter':r.reporter.id,
            'id_assignedto':r.assignedto.id,'id_ticket':r.id})
    # for x in Projects.objects.all():
    #     archivos_database[x.name] = {'users':[],'users_data':[]}
    #     for y in x.id_users.values('id','username'):
    #         if x.name in archivos_database:
    #             archivos_database[x.name]['users'].append(y['username'])
    #             archivos_database[x.name]['id_project'] = x.id
    #             archivos_database[x.name]['users_data'].append(y['id'])
    


    context['archivos_database'] = archivos_database
    success = True
    # else:
    #     success = False
    return HttpResponse(json.dumps(context), content_type="application/json")

