# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
 
# Two-sequence containing the different possible
# states of a todo item
STATUS_CHOICES = (
    ('Todo', 'Todo'),
    ('Doing', 'Doing'),
    ('Done', 'Done')
)
 
class Todo(models.Model):
     """
    Todo model.
 
    Contains the `title`, `description`, `status` and `updated` fields
    for a Todo item
    """
 
     user = models.ForeignKey(User, default=1)
     title = models.CharField(max_length=100, null=True)
     description = models.CharField(max_length=255, null=True)
     status = models.CharField(max_length=1, choices=STATUS_CHOICES,null=True)
     updated = models.DateTimeField(default=timezone.now)
 
def __unicode__(self):
    return self.title
