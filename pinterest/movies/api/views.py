from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from movies.models import Movie
from .serializers import MovieSerializer


@api_view(["GET"])
def movie_index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def movie_create(request):
    ser_movies = MovieSerializer(data=request.data)
    if ser_movies.is_valid():
        ser_movies.save()
    else:
        return Response(data=ser_movies.errors)
    return Response(data=ser_movies.data, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
def movie_delete(request, pk):
    response = {}
    try:
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        response['data'] = {'message': 'Deleted'}
        response['status'] = status.HTTP_200_OK
    except Exception as e:
        response['data'] = {'message': 'error'}
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(['PUT', 'PATCH'])
def movie_update(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except:
        return Response(data={'message': 'This movie does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        ser_movie = MovieSerializer(instance=movie, data=request.data)
    elif request.method == 'PATCH':
        ser_movie = MovieSerializer(
            instance=movie, data=request.data, partial=True)

    if ser_movie.is_valid():
        ser_movie.save()
    else:
        return Response(data=ser_movie.errors)
    return Response(data=ser_movie.data, status=status.HTTP_200_OK)
