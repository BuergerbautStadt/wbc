# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from projekte.models import Projekt, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

class ProjektAdmin(admin.ModelAdmin):
    list_display = ('id','bezeichner','adresse')
    list_display_links = ('id','bezeichner','adresse')
    fields = [ 'adresse' , 'bezirke', 'lat', 'lon', 'beschreibung', 'bezeichner'] 
    ordering = ['id']
    change_form_template = "projekte/admin/change_form.html"
    add_form_template = "projekte/admin/change_form.html"

class VeroeffentlichungAdminForm(forms.ModelForm):
    class Meta:
        model = Veroeffentlichung

    def __init__(self, *args, **kwds):
        super(VeroeffentlichungAdminForm, self).__init__(*args, **kwds)
        self.fields['verfahrensschritt'].queryset = Verfahrensschritt.objects

class VeroeffentlichungAdmin(admin.ModelAdmin):
    list_display = ('id','verfahrensschritt','projekt','ende')
    list_display_links = ('id','verfahrensschritt','projekt','ende')
    ordering = ['id']
    form = VeroeffentlichungAdminForm

class VerfahrensschrittAdmin(admin.ModelAdmin):
    list_display = ('id','name','reihenfolge','verfahren')
    list_display_links = ('id','name','reihenfolge','verfahren')
    ordering = ['id']

class VerfahrenAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

class BehoerdeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

class BezirkAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

admin.site.register(Projekt, ProjektAdmin)
admin.site.register(Veroeffentlichung, VeroeffentlichungAdmin)
admin.site.register(Verfahrensschritt, VerfahrensschrittAdmin)
admin.site.register(Verfahren, VerfahrenAdmin)
admin.site.register(Behoerde, BehoerdeAdmin)
admin.site.register(Bezirk, BezirkAdmin)
