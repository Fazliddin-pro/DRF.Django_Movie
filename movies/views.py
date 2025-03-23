from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer

class MovieListView(APIView):
    """Вывод списка фильмов"""
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MovieDetailView(APIView):
    """Вывод фильма"""
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.get(id=kwargs['pk'], draft=False)
        serializer = MovieDetailSerializer(movies)
        return Response(serializer.data, status=status.HTTP_200_OK)