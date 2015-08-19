# -*- encoding: utf-8 -*-
from django.db import models


class Person(models.Model):
    first_name = models.CharField("First Name", max_length=30)
    last_name = models.CharField("Last Name", max_length=30)
    birth_date = models.DateField("Date of Birth")
    con_email = models.EmailField("Email", max_length=79)
    con_jabbber = models.EmailField("Jabber", max_length=79)
    con_skype = models.CharField("Skype", max_length=79)
    bio = models.TextField("Bio", max_length=400)
    con_other = models.TextField("Other Contacts", max_length=400, blank=True)


class RequestCollect(models.Model):
    r_method = models.CharField(max_length=20, blank=True)
    r_path = models.CharField(max_length=90)
    r_time = models.DateTimeField(auto_now_add=True)
    r_read_id = models.IntegerField(blank=True)

    def __str__(self):
        return "%s   %s   '%s'" % (self.r_time.strftime('%d-%m-%Y %I:%M:%S'), self.r_method, self.r_path)
