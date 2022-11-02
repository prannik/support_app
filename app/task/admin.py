from django.contrib import admin

from app.task.models import Answer, Problem

admin.site.register(Problem)
admin.site.register(Answer)
