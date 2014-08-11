# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.timezone import utc
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.signal_handlers import generate_aliases_global
from easy_thumbnails.signals import saved_file
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class TopStory(CMSPlugin):
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name=_(u'Title'))

    def get_items(self):
        return TopStoryItem.objects.filter(active=True).order_by('ordering')

    def __unicode__(self):
        return self.title


class TopStoryItem(models.Model):
    TEASER_POSITION_CHOICES = (
        ('left', _(u'left')),
        ('right', _(u'right')),
    )

    PERCENTAGE_CHOICES = (
        (  0,   u'0%'),
        ( 10,  u'10%'),
        ( 20,  u'20%'),
        ( 30,  u'30%'),
        ( 40,  u'40%'),
        ( 50,  u'50%'),
        ( 60,  u'60%'),
        ( 70,  u'70%'),
        ( 80,  u'80%'),
        ( 90,  u'90%'),
        (100, u'100%'),
    )

    active = models.BooleanField(
        default=False,
        verbose_name=_(u'active'))

    topstory = models.ForeignKey(
        TopStory,
        related_name='topstory_items')

    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name=_(u'Title'))

    description = models.CharField(
        max_length=2048,
        blank=True,
        null=True,
        verbose_name=_(u'Description'))

    teaser_position = models.CharField(
        max_length=50,
        choices=TEASER_POSITION_CHOICES,
        verbose_name=_(u'Teaer Position'))

    focal_point_x = models.PositiveIntegerField(
        default=50,
        choices=PERCENTAGE_CHOICES,
        verbose_name=_(u'Focal Point (horizontal)'))

    focal_point_y = models.PositiveIntegerField(
        default=50,
        choices=PERCENTAGE_CHOICES,
        verbose_name=_(u'Focal Point (vertical)'))

    ordering = models.PositiveIntegerField(
        verbose_name=_(u'Ordering'))

    image = ThumbnailerImageField(
        upload_to='cms_news/',
        verbose_name=_(u'Image'))

    image_width = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        verbose_name=_(u'Original Image Width'))

    image_height = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        verbose_name=_(u'Original Image Height'))

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['ordering']
        verbose_name = _(u'Top Story Item')
        verbose_name_plural = _(u'Top Story Items')
