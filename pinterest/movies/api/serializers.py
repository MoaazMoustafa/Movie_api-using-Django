from rest_framework import serializers
from movies.models import Movie, Actor


class ActorSerializer(serializers.ModelSerializer):
    model = Actor
    fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # categories = serializers.StringRelatedField(many=True, read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)

    # actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
