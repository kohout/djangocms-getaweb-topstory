# -*- coding: utf-8 -*-
from django import forms
from django.db.models import Q
from django.conf import settings
from djangocms_topstory.models import TopStoryItem
from django.contrib.contenttypes.models import ContentType

f = None
for _ct in settings.THUMBNAIL_TOPSTORY_CONTENT_TYPES:
    if f is None:
        f = (Q(app_label=_ct[0]) & Q(model=_ct[1]))
    else:
        f = f | (Q(app_label=_ct[0]) & Q(model=_ct[1]))


class TopStoryItemForm(forms.ModelForm):
    content_type = forms.ModelChoiceField(
        initial=ContentType.objects.get(
            app_label=settings.THUMBNAIL_TOPSTORY_CT_DEFAULT[0],
            model=settings.THUMBNAIL_TOPSTORY_CT_DEFAULT[1]),
        queryset=ContentType.objects.filter(f))

    class Meta:
        model = TopStoryItem
        exclude = ()
