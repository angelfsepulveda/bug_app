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
from bug_app.models import *
from django.db.models import Q
import json
# Log
import logging
logger = logging.getLogger(__name__)
@login_required
def index(request):
    context={}
    context['app']                   = 'index'
    context['app_name']              = 'index'
    context['seccion']               = '%s_inicio_index' % (context['app'])
    context['navbar']                = True
    context['menu']                  = True
    context['footer']                = False
    context['user_id']               = request.user.id
    context['sidebar']               = False
    context['titulo']                = '%s: Inicio'
    context['btns_menu']             = True
    # context['regresar']              = reverse('autentificacion:inicio')
    context['user_username']         = User.objects.get(id=request.user.id).username
    context['user_rol']              = Users_info.objects.get(id_user=request.user.id).role
    logger.debug("############################################3")
    logger.debug("############################################3")
    logger.debug("user_id %s"%request.user.id)
    context['user_rol'] = role_choices[int(context['user_rol'])][1]
    logger.debug("user_rol %s"%context["user_rol"])
    # first chart, total number of tickers bar chart by priority
    list_data = []
    dict_tickets = Tickets.objects.filter(priority=0).values()
    list_data.append(['None',len(dict_tickets)])
    dict_tickets = {}
    dict_tickets = Tickets.objects.filter(priority=1).values()
    list_data.append(['Low',len(dict_tickets)])
    dict_tickets = {}
    dict_tickets = Tickets.objects.filter(priority=2).values()
    list_data.append(['Medium',len(dict_tickets)])
    dict_tickets = {}
    dict_tickets = Tickets.objects.filter(priority=3).values()
    list_data.append(['High',len(dict_tickets)])
    context['list_data'] = json.dumps(list_data)
    # end first chart
    # second chart total number of tickets resolved
    dict_tickets = {}
    list_data = []
    dict_tickets = Tickets.objects.filter(priority=0,status=3).values()
    list_data.append(['None',len(dict_tickets)])
    dict_tickets = {}
    dict_tickets = Tickets.objects.filter(priority=1,status=3).values()
    list_data.append(['Low',len(dict_tickets)])
    dict_tickets = {}
    dict_tickets = Tickets.objects.filter(priority=2,status=3).values()
    list_data.append(['Medium',len(dict_tickets)])
    dict_tickets = {}
    dict_tickets = Tickets.objects.filter(priority=3,status=3).values()
    list_data.append(['High',len(dict_tickets)])
    context['list_data_resolved'] = json.dumps(list_data)
    # end second chart
    #start third chart pie chart by type
    list_data = []
    dict_tickets = {}
    dict_tickets = Tickets.objects.filter(typeticket=0).values()
    list_data.append(['Bug',len(dict_tickets)])
    dict_tickets = {}
    dict_tickets = Tickets.objects.filter(typeticket=1).values()
    list_data.append(['Error',len(dict_tickets)])
    context['list_data_type'] = json.dumps(list_data)

    return render(request, 'bug_app/templates/index.html', context)