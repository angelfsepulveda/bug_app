from django import forms 
from .models import *
from django.contrib.auth.models import User
from django.contrib.admin import widgets
#
selectpicker_widgets_solo = {
    'class':"selectpicker form-control form-control-sm",
    'data-none-selected-text':"No hay opciones seleccionadas",
    'data-actions-box':"true",
    'data-size':"10",
    'data-dropup-auto':"false",
    #'multiple':"",
    'data-live-search':"true",
}
selectpicker_widgets_mult = {
    'class':"selectpicker form-control form-control-sm",
    'data-none-selected-text':"No hay opciones seleccionadas",
    'data-actions-box':"true",
    'data-size':"10",
    'data-dropup-auto':"false",
    'multiple':"",
    'data-live-search':"true",
}
class UsersForm(forms.Form):
    # username    = forms.CharField(max_length = 255, label = "Username", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter Username'}))
    password    = forms.CharField(max_length = 255, label = "Password:", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter password'}))
    first_name  = forms.CharField(max_length = 255, label = "First name:", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter First name'}))
    last_name   = forms.CharField(max_length = 255, label = "Last name:", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter Last name'}))
    email       = forms.EmailField(max_length = 255, label = "Email:", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter email'}))
    role        = forms.ChoiceField(choices = role_choices,widget=forms.Select(attrs=selectpicker_widgets_solo))


class ProjectsForm(forms.Form): 
    name        = forms.CharField(max_length = 255, label = "project Name", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter name'}))
    id_users    = forms.ModelMultipleChoiceField(queryset = User.objects.all().exclude(id=1),widget=forms.Select(attrs=selectpicker_widgets_mult))

class TicketForm(forms.Form):
    name                = forms.CharField(max_length = 255, label = "Name:", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter name'}))
    description         = forms.CharField(max_length = 255, label = "Description:", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter description'}))
    priority            = forms.ChoiceField(choices = priority_choices,label = "Priority of ticket:",widget=forms.Select(attrs=selectpicker_widgets_solo))
    status              = forms.ChoiceField(choices = status_choices,label = "Status of ticket:",widget=forms.Select(attrs=selectpicker_widgets_solo))
    typeticket          = forms.ChoiceField(choices = type_choices,label = "Type of ticket:",widget=forms.Select(attrs=selectpicker_widgets_solo))
    reporter            = forms.ModelChoiceField(queryset = User.objects.all().exclude(id=1),label = "Reported by:" ,widget=forms.Select(attrs=selectpicker_widgets_solo))
    assignedto          = forms.ModelChoiceField(queryset = User.objects.all().exclude(id=1),label = "Assigned to:" ,widget=forms.Select(attrs=selectpicker_widgets_solo))
    version_reported    = forms.CharField(max_length = 255, label = "Version reported:", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter version reported'}))
    fixed_version       = forms.CharField(max_length = 255, label = "Fixed in version:", widget=forms.TextInput(attrs={'class': "form-control required",'placeholder':'Enter fixed in version'}))
    project_id          = forms.ModelChoiceField(queryset = Projects.objects.all(),label = "Project name:",widget=forms.Select(attrs=selectpicker_widgets_solo))