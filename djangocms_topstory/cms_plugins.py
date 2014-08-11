from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_topstory.models import TopStory
from djangocms_topstory.admin import TopStoryItemInline

class TopStoryPlugin(CMSPluginBase):
    model = TopStory
    name = _("Top-Story")
    render_template = "cms/plugins/topstory/index.html"
    inlines = [TopStoryItemInline]

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['items'] = instance.get_items()
        return context

plugin_pool.register_plugin(TopStoryPlugin)
