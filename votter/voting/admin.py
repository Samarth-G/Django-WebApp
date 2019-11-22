from django.contrib import admin
from .models import Questions, Choice

admin.site.site_header = "-- Votter Admin --"
admin.site.site_title = "Votter Admin Page"
admin.site.index_title = "Welcome to the Backend"

class ChoiceInLine(admin.TabularInline):

    model = Choice
    extra = 3

class QuestionsAdmin(admin.ModelAdmin):

    fieldsets = [(None, {'fields':['questionText']}),
                 ('Date Info', {'fields': ['pubDate'],
                                'classes':['collapse']}),]

    inlines = [ChoiceInLine]

admin.site.register(Questions, QuestionsAdmin)