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
from bug_app.forms import *
# Log
import logging
logger = logging.getLogger(__name__)

def register(request):
    context={}
    context['app']                   = 'register'
    context['app_name']              = 'register'
    context['seccion']               = '%s_inicio_login' % (context['app'])
    context['navbar']                = True
    context['menu']                  = True
    context['footer']                = False
    context['user_id']               = request.user.id
    context['sidebar']               = False
    context['titulo']                = '%s: register'
    context['btns_menu']             = True
    # context['regresar']              = reverse('autentificacion:inicio')
    context['UsersForm']              = UsersForm()
    
    return render(request, 'bug_app/templates/register.html', context)