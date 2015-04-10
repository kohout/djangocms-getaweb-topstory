# -*- coding: utf-8 -*-
from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from django.contrib import admin
from djangocms_topstory.models import TopStory, TopStoryItem
from djangocms_topstory.forms import TopStoryItemForm
from adminsortable.admin import SortableInlineAdminMixin


class TopStoryItemInline(SortableInlineAdminMixin, admin.TabularInline):
    fields = ('active', 'title', 'image', 'ordering', )
    model = TopStoryItem
    extra = 0
    sortable_field_name = 'ordering'

class TopStoryAdmin(admin.ModelAdmin):
    inlines = [TopStoryItemInline]

class TopStoryItemAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    form = TopStoryItemForm
    fieldsets = (
        (None, {
            'fields': (
                ('active', ),
                ('title', 'teaser_position', ),
                ('description', 'teaser_layout', ),
                ('content_type', 'object_id', ),
                ('external_url', ),
            ),
        }),
    )

admin.site.register(TopStory, TopStoryAdmin)
admin.site.register(TopStoryItem, TopStoryItemAdmin)
