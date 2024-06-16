from rest_framework import serializers
from django.contrib.auth.models import User
from .models import todo
from django.core.validators import MaxValueValidator, MinValueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('name','priorty','progress')