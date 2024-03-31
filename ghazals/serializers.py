from rest_framework import serializers
from .models import Poem,PoemReactions
from django.contrib.auth.models import User


class PoemSerializer(serializers.ModelSerializer):
    posted_by = serializers.ReadOnlyField(source='posted_by.username')
    reacted_by_user = serializers.SerializerMethodField(read_only=True)
    reaction = serializers.CharField(read_only=True)
    react_count = serializers.IntegerField(read_only=True)

    def get_reacted_by_user(self,obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            reaction_instance = PoemReactions.objects.filter(poem=obj, reacted_by=request.user).first()
            if reaction_instance:
                return reaction_instance.reaction
        return None

    class Meta:
        model = Poem
        fields = '__all__'



class PoemReactionsSerializer(serializers.ModelSerializer):
    reacted_by = serializers.ReadOnlyField(source='reacted_by.username')
    poem = serializers.ReadOnlyField(source='poem.id') 

    class Meta:
        model = PoemReactions
        fields = '__all__'

 
class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Poem.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'poems')