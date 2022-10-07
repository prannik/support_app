from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from app.task.filters import ProblemFilter
from app.task.models import Answer, Problem
from app.task.serializer import (CreateAnswerSerializer, CreateProblemSerializer, ListAnswerSerializer,
                                 ListProblemSerializer, RetrieveProblemSerializer)


class ProblemViewSet(GenericViewSet):
    queryset = Problem.objects.all().order_by('date_publish')
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = ProblemFilter
    search_fields = ('title_problem', 'text_problem')
    serializer_classes = {
        'create': CreateProblemSerializer,
        'list': ListProblemSerializer,
        'retrieve': RetrieveProblemSerializer,
    }
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        answers = Answer.objects.filter(response_tag=pk)
        instance.answers = answers
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, Serializer)


class AnswerViewSet(GenericViewSet):
    queryset = Answer.objects.all().order_by('-date_publish')
    permission_classes = [IsAuthenticated]
    serializer_classes = {
        'create': CreateAnswerSerializer,
        'list': ListAnswerSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, Serializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
