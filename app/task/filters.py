from django_filters.rest_framework import FilterSet

from app.task.models import Problem


class ProblemFilter(FilterSet):
    class Meta:
        model = Problem
        fields = ('status_problem', 'author')
