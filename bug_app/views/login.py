# -*- coding: utf-8 -*-
from django.shortcuts import  redirect, render, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.urls import reverse, reverse_lazy
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import generic
from django.contrib.auth.models import User,Permission
from django.core.serializers.json import DjangoJSONEncoder
from bug_app.models import *
from django.db.models import Q
import json
# Log
import logging
logger = logging.getLogger(__name__)

def login(request):
    context={}
    context['app']                   = 'login'
    context['app_name']              = 'login'
    context['seccion']               = '%s_inicio_login' % (context['app'])
    context['navbar']                = True
    context['menu']                  = True
    context['footer']                = False
    context['user_id']               = request.user.id
    context['sidebar']               = False
    context['titulo']                = '%s: login'
    context['btns_menu']             = True
    # context['regresar']              = reverse('autentificacion:inicio')
    
    return render(request, 'bug_app/templates/login.html', context)