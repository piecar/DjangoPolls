from django.contrib import admin

from .models import Question

# Tells admin that Question objects have admin interface

admin.site.register(Question)