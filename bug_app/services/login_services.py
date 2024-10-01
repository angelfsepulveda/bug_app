from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_user
from bug_app.models import *
import json, datetime
from datetime import datetime
#logger
import logging
logger = logging.getLogger(__name__)

def login_services(request):
    context = {}
    success = None    
    logger.debug('***********************')
    logger.debug("bug_app_login_services")
    logger.debug(request.POST)
    password    = request.POST['password']
    email       = request.POST['email']
    logout(request)
    users = User.objects.get(email=email).username
    logger.debug("users: ")
    logger.debug(users)
    user = authenticate(username=users,password=password)    
    if user is not None:
        if user.is_active:
            logger.debug("user is active")
            login_user(request, user)
            request.session['user_id']    = user.pk
            request.session['username']   = user.username
            request.session['nombre']     = user.first_name
            request.session['apellido']   = user.last_name
            request.session['is_staff']   = user.is_staff
            ####
            success = True
        else:
            messages = 'This account is disabled, contact the admin'
            context['messages'] = messages
    else:
        messages = 'User or password incorrect.'
        context['messages'] = messages
    context['success'] = success
    
    return HttpResponse(json.dumps(context), content_type="application/json")