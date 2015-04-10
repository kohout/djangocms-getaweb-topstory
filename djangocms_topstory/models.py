# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
from easy_thumbnails.fields import ThumbnailerImageField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from gfklookupwidget.fields import GfkLookupField

_THUMBNAIL_TOPSTORY_DEFAULT = getattr(settings,
    'THUMBNAIL_TOPSTORY_DEFAULT', None)

if _THUMBNAIL_TOPSTORY_DEFAULT is None:
    _THUMBNAIL_TOPSTORY_DEFAULT = settings.THUMBNAIL_TOPSTORY_CHOICES[0][0]

class TopStory(CMSPlugin):
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name=_(u'Title'))

    width = models.CharField(
        max_length=10,
        default='100%',
        verbose_name=_(u'Width of plugin')
    )

    height = models.CharField(
        max_length=10,
        default='434px',
        verbose_name=_(u'Height of plugin')
    )

    def get_items(self):
        return TopStoryItem.objects.filter(active=True,
            topstory=self).order_by('ordering')

    def copy_relations(self, old_instance):
        for topstory_item in old_instance.topstory_items.all():
            topstory_item.pk = None
            topstory_item.topstory = self
            topstory_item.save()

    def __unicode__(self):
        return self.title


class TopStoryItem(models.Model):
    TEASER_POSITION_CHOICES = (
        ('left', _(u'left')),
        ('right', _(u'right')),
    )

    TEASER_LAYOUT_CHOICES = (
        ('white', _(u'Weißer Hintergrund, Schwarze Schrift')),
        ('black', _(u'Schwarzer Hintergrund, Weiße Schrift')),
        ('green', _(u'Grüner Hintergrund, Graue Schrift')),
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
        default=TEASER_POSITION_CHOICES[0][0],
        verbose_name=_(u'Teaser Position'))

    teaser_layout = models.CharField(
        max_length=100,
        choices=TEASER_LAYOUT_CHOICES,
        default=TEASER_LAYOUT_CHOICES[0][0],
        verbose_name=_(u'Teaser Layout')
    )

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

    size = models.CharField(
        choices=settings.THUMBNAIL_TOPSTORY_CHOICES,
        default=_THUMBNAIL_TOPSTORY_DEFAULT,
        max_length=50,
        verbose_name=_(u'Image size and scale')
    )

    content_type = models.ForeignKey(ContentType,
        verbose_name=u'Link-Typ',
        blank=True, null=True)
    #object_id = models.PositiveIntegerField(blank=True, null=True)
    object_id = GfkLookupField(
        'content_type',
        null=True, blank=True,
        verbose_name=u'Link-Ziel',
    )
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    external_url = models.URLField(
        blank=True, null=True,
        verbose_name=u'Externe URL')

    def save(self, *args, **kwargs):
        if self.topstory:
            self.topstory.save()
        return super(TopStoryItem, self).save(*args, **kwargs)

    class Meta:
        ordering = ['ordering']
        verbose_name = _(u'Top Story Item')
        verbose_name_plural = _(u'Top Story Items')
