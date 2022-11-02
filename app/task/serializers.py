from rest_framework import serializers

from app.task.models import Answer, Problem
from app.task.task import send_update_status


class CreateProblemSerializer(serializers.ModelSerializer):
    """ Serializer creation Question """

    class Meta:
        model = Problem
        fields = ('author', 'title', 'description')

    def create(self, validated_data):
        self.instance = Problem.objects.create(author=self.context['request'].user, **validated_data)
        return self.instance


class ListProblemSerializer(serializers.ModelSerializer):
    """ Serializer list of all questions"""

    class Meta:
        model = Problem
        fields = ('author', 'title', 'status', 'date_created', 'id')


class CreateAnswerSerializer(serializers.ModelSerializer):
    """ Serializer creation Answer """
    response_problem = serializers.SlugRelatedField(slug_field='pk', queryset=Problem.objects.all())

    class Meta:
        model = Answer
        fields = ('author', 'text', 'response_problem')

    def create(self, validated_data):
        self.instance = Answer.objects.create(author=self.context['request'].user, **validated_data)
        return self.instance


class ListAnswerSerializer(serializers.ModelSerializer):
    """ Serializer list of all answers"""

    class Meta:
        model = Answer
        fields = ('author', 'text', 'date_created', 'response_problem')


class RetrieveProblemSerializer(serializers.ModelSerializer):
    """ Serializer full specific question """
    answers = ListAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Problem
        fields = ('author', 'status', 'title', 'description', 'date_created', 'answers')


class UpdateStatusProblemSerializer(serializers.ModelSerializer):
    """ Serializer update status  """
    status = serializers.ChoiceField(choices=Problem.Status)
    author = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    date_created = serializers.CharField(read_only=True)

    class Meta:
        model = Problem
        fields = ('author', 'status', 'title', 'description', 'date_created')

    def update(self, instance, validated_data):
        status = dict(Problem.Status.choices).get(instance.status)
        send_update_status.delay(instance.title, status, instance.author.email)
        return instance
