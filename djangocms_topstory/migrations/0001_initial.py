# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import gfklookupwidget.fields
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopStory',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Titel', blank=True)),
                ('width', models.CharField(default=b'100%', max_length=10, verbose_name='Width of plugin')),
                ('height', models.CharField(default=b'434px', max_length=10, verbose_name='Height of plugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TopStoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False, verbose_name='Aktiv')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Titel', blank=True)),
                ('description', models.CharField(max_length=2048, null=True, verbose_name='Beschreibung', blank=True)),
                ('teaser_position', models.CharField(default=b'left', max_length=50, verbose_name='Teaser Position', choices=[(b'left', 'Links'), (b'right', 'Rechts')])),
                ('teaser_layout', models.CharField(default=b'white', max_length=100, verbose_name='Teaser Layout', choices=[(b'white', 'Wei\xdfer Hintergrund, Schwarze Schrift'), (b'black', 'Schwarzer Hintergrund, Wei\xdfe Schrift'), (b'green', 'Gr\xfcner Hintergrund, Graue Schrift')])),
                ('focal_point_x', models.PositiveIntegerField(default=50, verbose_name='Focal Point (horizontal)', choices=[(0, '0%'), (10, '10%'), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'), (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')])),
                ('focal_point_y', models.PositiveIntegerField(default=50, verbose_name='Focal Point (vertical)', choices=[(0, '0%'), (10, '10%'), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'), (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')])),
                ('ordering', models.PositiveIntegerField(verbose_name='Sortierung')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'cms_news/', verbose_name='Bild')),
                ('image_width', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Breite des Originalbildes')),
                ('image_height', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='H\xf6he des Originalbildes')),
                ('size', models.CharField(default=b'fullscreen', max_length=50, verbose_name='Image size and scale', choices=[(b'logo', '250x55, ohne crop'), (b'masonry', '300x800, ohne crop'), (b'normal', '420x280, mit crop, aufskaliert'), (b'main', '814x300, mit crop, aufskaliert'), (b'fullsize', '800x600, ohne crop'), (b'fullscreen', '1680x640, mit crop, aufskaliert')])),
                ('object_id', gfklookupwidget.fields.GfkLookupField(default=None, null=True, verbose_name='Link-Ziel', blank=True)),
                ('external_url', models.URLField(null=True, verbose_name='Externe URL', blank=True)),
                ('content_type', models.ForeignKey(verbose_name='Link-Typ', blank=True, to='contenttypes.ContentType', null=True)),
                ('topstory', models.ForeignKey(related_name='topstory_items', to='djangocms_topstory.TopStory')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Top Story Item',
                'verbose_name_plural': 'Top Story Items',
            },
        ),
    ]
