from rest_framework import serializers
from .models import Movie, Rating, Actor, Producer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only':True, 'required':True}}#we can't see password by GET but he still required

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)#creating user
        Token.objects.create(user=user)
        return user

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'surname')

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ('id', 'name', 'surname')

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    producers = ProducerSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating', 'country', 'genre', 'year', 'actors',
                  'producers')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')