# -*- coding: utf-8 -*-
import logging

LOG = logging.getLogger(__name__)

import itertools
from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Profile(models.Model):
    """
    Extention of User
    """

    user = models.OneToOneField(
        User, default=1)
    profile_picture = models.CharField(default="", max_length=150, blank=True)
    screen_name = models.CharField(default="", max_length=50, blank=True)


class Organization(models.Model):
    """
    Extention of User
    """

    name = models.CharField(blank=False, max_length=64)
    website = models.CharField(default="", blank=True, max_length=64)
    contact = models.CharField(default="", blank=True, max_length=64)
    trusted_users = models.ManyToManyField('TrustedUser', through='Membership', blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class TrustedUser(models.Model):
    """
    Extention of User
    """

    user = models.OneToOneField(
        User, default=1, unique=True)
    organizations = models.ManyToManyField('Organization', through=Organization.trusted_users.through, blank=True)


class Membership(models.Model):
    organisation = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(TrustedUser, on_delete=models.CASCADE)
    date_added = models.DateField()
    invite_reason = models.CharField(max_length=64, blank=True)
