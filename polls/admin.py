from django.contrib import admin

from .models import Question, Choice

# Tells Django choices are edited in the Question page, with default 3 choices.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

# Tells admin that Question objects have admin interface
class QuestionAdmin(admin.ModelAdmin):
    # Let's you put field information on Question page
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    # Let's you order the fields in the detail page
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)