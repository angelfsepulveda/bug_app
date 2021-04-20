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

def show_project_services(request):
    context = {}
    logger.debug("show_project_services")
    # archivo_excel          = request.POST['archivo_excel']
    # logger.debug(fecha_quarter)
        # fechacompra = r.fechacompra.strftime('%d/%m/%Y')
     # fechaexpira = r.fechaexpira.strftime('%d/%m/%Y')
    # archivos_database.setdefault(r.id,{'nombre':r.nombre,'cantidad':r.cantidad,'preciocompra':r.preciocompra,'ganancia':r.ganancia,'fechacompra':fechacompra,'fechaexpira':fechaexpira,'categoria':r.categoria,'perdido':r.perdido})
    archivos_database={}
    for x in Projects.objects.all():
        archivos_database[x.name] = {'users':[],'users_data':[]}
        for y in x.id_users.values('id','username'):
            if x.name in archivos_database:
                archivos_database[x.name]['users'].append(y['username'])
                archivos_database[x.name]['id_project'] = x.id
                archivos_database[x.name]['users_data'].append(y['id'])
    


    context['archivos_database']=archivos_database
    success = True
    # else:
    #     success = False
    return HttpResponse(json.dumps(context), content_type="application/json")

