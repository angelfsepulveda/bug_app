"""tortas_bernal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import logout_then_login
from django.contrib import admin
from django.urls import path
# views
from bug_app.views.index import index
from bug_app.views.login import login
from bug_app.views.register import register
from bug_app.views.create import create
from bug_app.views.create_ticket import create_ticket

#services
from bug_app.services.register_services import register_services
from bug_app.services.login_services import login_services
from bug_app.services.save_project_services import save_project_services
from bug_app.services.show_project_services import show_project_services
from bug_app.services.delete_project_services import delete_project_services
from bug_app.services.create_ticket_services import create_ticket_services
from bug_app.services.show_ticket_services import show_ticket_services
from bug_app.services.delete_ticket_services import delete_ticket_services


app_name='bug_app'
urlpatterns = [
    #views path
    path('', login, name='login'),
    path('login', login, name='login'),
    path('index', index, name='index'),
    path('register', register, name='register'),
    path('create', create, name='create'),
    path('create_ticket', create_ticket, name='create_ticket'),
    # path('charts', charts, name='charts'),

    #services path
    path('register_services',register_services,name="register_services"),
    path('login_services',login_services,name="login_services"),
    path('logout', logout_then_login, {'login_url':'bug_app:login'}, name='logout'),
    path('save_project_services',save_project_services,name="save_project_services"),
    path('show_project_services',show_project_services,name="show_project_services"),
    path('delete_project_services',delete_project_services,name="delete_project_services"),
    path('create_ticket_services',create_ticket_services,name="create_ticket_services"),
    path('show_ticket_services',show_ticket_services,name="show_ticket_services"),
    path('delete_ticket_services',delete_ticket_services,name="delete_ticket_services"),
]