from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pubdate']
    list_display = ['question_text', 'pubdate', 'was_published_recently']
    search_fields = ['quesrion_text']
    fieldsets = [('Question Text', {'fields': ['question_text']}),
                 ('Publication Date', {'fields': ['pubdate'], 'classes': ['collapse']}),
                 ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

