# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Veninfo(models.Model):
    #this table stores the VEN information
    #column: VEN_NAME (chart), VEN_ID (char)
    ven_name=models.CharField(max_length=50)
    ven_id=models.CharField(max_length=50)
    def __str__(self):
        return self.ven_name,self.ven_id
