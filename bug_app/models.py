import datetime
import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.
role_choices = [
    ("0", "Project manager"),
    ("1", "Developer"),
]
priority_choices = [
    ("0", "None"),
    ("1", "Low"),
    ("2", "Medium"),
    ("3", "High"),
]
type_choices = [
    ("0", "Bug"),
    ("1", "Error"),
]
status_choices = [
    ("0", "New"),
    ("1", "Open"),
    ("2", "In progress"),
    ("3", "Resolved"),
    ("4", "Additional info required"),
]

class Users_info(models.Model):
    id_user    = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "id_user_users_info")
    role       = models.CharField(max_length = 1,choices = role_choices,null=False,blank=False)
    class Meta:
        app_label              = "bug_app"
        verbose_name           = u'Users_info: information'
        verbose_name_plural    = u'Users_info: information'
        ordering               = ('id',)
    def __unicode__(self):
        return u"%s" % (self.id_user)
    def __str__(self):
        return u"%s" % (self.id_user)

class Projects(models.Model):
    name        = models.CharField(max_length = 255)
    id_users    = models.ManyToManyField(User, related_name = "id_users_projects")
    class Meta:
        app_label              = "bug_app"
        verbose_name           = u'Project: information'
        verbose_name_plural    = u'Projects: information'
        ordering               = ('id',)
    def __unicode__(self):
        return u"%s" % (self.name)
    def __str__(self):
        return u"%s" % (self.name)

class Tickets(models.Model):
    name                 = models.CharField(max_length = 255)
    description          = models.CharField(max_length = 255)
    priority             = models.CharField(max_length = 1,choices = priority_choices, default = 0)
    status               = models.CharField(max_length = 1,choices = status_choices, default = 0)
    typeticket           = models.CharField(max_length = 1,choices = type_choices, default = 0)
    reporter             = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "id_user_tickets_reporter")
    assignedto           = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "id_user_tickets_assignedto")
    version_reported     = models.CharField(max_length = 255,blank=True,null=True)
    fixed_version        = models.CharField(max_length = 255, blank=True,null=True)
    date_submitted       = models.DateTimeField(auto_now_add=True)
    project_id           = models.ForeignKey(Projects, on_delete = models.CASCADE, related_name = "id_user_tickets_projects")
    class Meta:
        app_label              = "bug_app"
        verbose_name           = u'Ticket: information'
        verbose_name_plural    = u'Tickets: information'
        ordering               = ('id',)
    def __unicode__(self):
        return u"%s" % (self.name)
    def __str__(self):
        return u"%s" % (self.name)


