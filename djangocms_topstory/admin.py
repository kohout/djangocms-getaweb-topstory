from django.contrib import admin
from djangocms_topstory.models import TopStory, TopStoryItem
from adminsortable.admin import SortableInlineAdminMixin


class TopStoryItemInline(SortableInlineAdminMixin, admin.TabularInline):
    fields = ('active', 'title', 'description', 'teaser_position', 'teaser_layout',
        'focal_point_x', 'focal_point_y', 'image', 'size', 'content_type',
        'object_id', 'ordering', )
    model = TopStoryItem
    extra = 0
    sortable_field_name = 'ordering'

class TopStoryAdmin(admin.ModelAdmin):
    inlines = [TopStoryItemInline]

admin.site.register(TopStory, TopStoryAdmin)
admin.site.register(TopStoryItem)
