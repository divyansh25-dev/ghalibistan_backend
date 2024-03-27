from rest_framework import serializers
from .models import Ghazal,Discussion,Reaction
from django.contrib.auth.models import User

class GhazalSerializer(serializers.ModelSerializer):
    posted_by = serializers.ReadOnlyField(source='posted_by.username')

    class Meta:
        model = Ghazal
        fields = ('id','name','interpretation','created_at','posted_by')

class UserSerializer(serializers.ModelSerializer):
    ghazals = serializers.PrimaryKeyRelatedField(many=True,queryset=Ghazal.objects.all())

    class Meta:
        model = User
        fields = ('id' , 'username', 'ghazals')


class DiscussionSerializer(serializers.ModelSerializer):
    ghazal = serializers.ReadOnlyField(source='ghazal.id')
    commented_by = serializers.ReadOnlyField(source='commented_by.username')

    class Meta:
        model = Discussion
        fields = '__all__'

class ReactionSerializer(serializers.ModelSerializer):
    reacted_by = serializers.ReadOnlyField(source='reacted_by.id')
    discussion = serializers.ReadOnlyField(source='discussion.id')

    class Meta:
        model = Reaction
        fields = '__all__'





