from django.shortcuts import render
from rest_framework import generics, permissions
from .models import *
from .serializers import *

class MovieListAPI(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MovieCreateAPI(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MovieUpdate(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MovieDelete(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ActorListAPI(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ActorCreateAPI(generics.CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ActorUpdate(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ActorDelete(generics.DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GenreListAPI(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GenreCreateAPI(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GenreUpdate(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GenreDelete(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DirectorListAPI(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DirectorCreateAPI(generics.CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DirectorUpdate(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DirectorDelete(generics.DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewerListAPI(generics.ListAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewerCreateAPI(generics.CreateAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewerUpdate(generics.RetrieveAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewerDelete(generics.DestroyAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
