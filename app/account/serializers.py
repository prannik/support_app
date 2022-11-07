from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from app.account.models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    """ User`s sign up serializer """

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=256, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'token')

    def create(self, validated_data):
        self.instance = get_user_model().objects.create_user(**validated_data)
        return self.instance


class LogInSerializer(serializers.ModelSerializer):
    """ User`s log in serializer """

    email = serializers.EmailField()
    username = serializers.CharField(max_length=128, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=128, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'token')

    def validate(self, attrs):
        try:
            self.instance = get_user_model().objects.filter(is_active=True).get(email=attrs.get('email'))
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError({'email': 'No such user.'})
        if not self.instance.check_password(attrs.get('password')):
            raise serializers.ValidationError({'password': 'Wrong password.'})
        return attrs


class SignUpStaffSerializer(serializers.ModelSerializer):
    """ Staff sign up serializer """

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=256, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'token')

    def create(self, validated_data):
        self.instance = get_user_model().objects.create_staff(**validated_data)
        return self.instance
