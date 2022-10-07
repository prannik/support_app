from rest_framework import serializers

from app.task.models import Answer, Problem


class CreateProblemSerializer(serializers.ModelSerializer):
    """ Serializer creation Question """
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Problem
        fields = ('author', 'title_problem', 'text_problem')

    def create(self, validated_data):
        self.instance = Problem.objects.create(author=self.context['request'].user, **validated_data)
        return self.instance


class ListProblemSerializer(serializers.ModelSerializer):
    """ Serializer list of all questions"""

    class Meta:
        model = Problem
        fields = ('author', 'title_problem', 'status_problem', 'date_publish', 'id')


class CreateAnswerSerializer(serializers.ModelSerializer):
    """ Serializer creation Answer """
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    response_tag = serializers.SlugRelatedField(slug_field='pk', queryset=Problem.objects.all())

    class Meta:
        model = Answer
        fields = ('author', 'text_discussion', 'response_tag')

    def create(self, validated_data):
        self.instance = Answer.objects.create(author=self.context['request'].user, **validated_data)
        return self.instance


class ListAnswerSerializer(serializers.ModelSerializer):
    """ Serializer list of all answers"""

    class Meta:
        model = Answer
        fields = ('author', 'text_discussion', 'date_publish', 'response_tag')


class RetrieveProblemSerializer(serializers.ModelSerializer):
    """ Serializer full specific question """
    answers = ListAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Problem
        fields = ('author', 'status_problem', 'title_problem', 'text_problem', 'date_publish', 'answers')
