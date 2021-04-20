# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.urls import reverse, reverse_lazy
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import generic
from django.contrib.auth.models import User,Permission
from django.core.serializers.json import DjangoJSONEncoder
import json
from bug_app.models import *
from django.db.models import Q
from bug_app.forms import *
# Log
import logging
logger = logging.getLogger(__name__)
@login_required
def create(request):
    context={}
    context['app']                   = 'create'
    context['app_name']              = 'create'
    context['seccion']               = '%s_inicio_create' % (context['app'])
    context['navbar']                = True
    context['menu']                  = True
    context['footer']                = False
    context['user_id']               = request.user.id
    context['sidebar']               = False
    context['titulo']                = '%s: create'
    context['btns_menu']             = True
    # context['regresar']              = reverse('autentificacion:inicio')
    context['ProjectsForm']          = ProjectsForm()
    context['user_username']         = User.objects.get(id=request.user.id).username
    context['user_rol']              = Users_info.objects.get(id_user=request.user.id).role
    logger.debug("############################################3")
    logger.debug("############################################3")
    logger.debug("user_id %s"%request.user.id)
    context['user_rol'] = role_choices[int(context['user_rol'])][1]
    logger.debug("user_rol %s"%context["user_rol"])


    return render(request, 'bug_app/templates/create.html', context)