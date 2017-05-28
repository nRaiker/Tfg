# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):
    propietario = models.CharField(max_length=100)
    docfile = models.FileField(upload_to='documents')

    def __str__(self):
        return self.docfile.name