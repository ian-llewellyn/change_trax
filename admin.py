from change_trax.models import Change, Problem
from django.contrib import admin

#class ProblemInline(admin.TabularInline):
#    model = Problem

class ChangeAdmin(admin.ModelAdmin):
    list_display = ['date', 'implementer', 'equipment', 'description']
    list_filter = ['date', 'equipment']
    search_fields = ['equipment', 'description']
    date_hierarchy = 'date'
    #inlines = [ProblemInline]

admin.site.register(Change, ChangeAdmin)

class ProblemAdmin(admin.ModelAdmin):
    list_display = ['date', 'description']
    list_filter = ['date']
    search_fields = ['description']
    date_hierarchy = 'date'

admin.site.register(Problem, ProblemAdmin)

