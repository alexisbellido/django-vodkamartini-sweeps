from django.contrib import admin
from .models import Sweep, SweepEntry

class SweepAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    #list_filter = ['created', 'status']
    #search_fields = ['title']
    #list_display = ('__unicode__', 'author', 'created', 'status')

class SweepEntryAdmin(admin.ModelAdmin):
    pass
    #list_display = ('__unicode__', 'quiz')
    #raw_id_fields = ('quiz',)

    #fields = ('question', ('quiz', 'editquiz'), 'enabled', 'weight')
    #readonly_fields = ('editquiz',)

    #def editquiz(self, instance):
    #    return '<a href="%s">%s</a>' % (reverse('admin:vodkamartiniquiz_quiz_change', args=(instance.quiz.id,)), instance.quiz.title)

    #editquiz.allow_tags = True
    #editquiz.short_description = 'Edit quiz'

    #readonly_fields = ('user', 'quiz', 'answer')

    #def question(self, instance):
    #    return instance.answer.question

admin.site.register(Sweep, SweepAdmin)
admin.site.register(SweepEntry, SweepEntryAdmin)
