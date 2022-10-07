from django.contrib import admin

from app.task.models import Answer, Problem


class ProblemAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Answer, AnswerAdmin)
