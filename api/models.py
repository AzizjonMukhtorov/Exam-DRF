from django.db import models
from django.utils import timezone
from django import forms
from django_enum_choices.fields import EnumChoiceField
from enum import Enum


LANGUAGE = (
    ('Russian', 'Russian'),
    ('Tajik', 'Tajik'),
    ('English', 'English')
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Movie(models.Model):
    movie_titile = models.CharField(max_length=250)
    movie_year = models.IntegerField()
    movie_time = models.TimeField()
    movie_lang = models.CharField(max_length=50, choices=LANGUAGE)
    movie_dt_rel = models.DateField()
    movie_country = models.CharField(max_length=50)


class Actor(models.Model):
    actor_name = models.CharField(max_length=50)
    actor_lastname = models.CharField(max_length=50)
    actor_gender = models.CharField(max_length=50, choices=GENDER)


class Genre(models.Model):
    gen_title = models.CharField(max_length=255)


class Director(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)


class Reviewer(models.Model):
    rev_name = models.CharField(max_length=50)


class MovieCast(models.Model):
    actor = models.ForeignKey(Actor, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    role = models.CharField(max_length=50)


class MovieDirector(models.Model):
    director = models.ForeignKey(Director, on_delete = models.CASCADE)
    movie = models.ForeignKey(Actor, on_delete = models.CASCADE)


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    review = models.ForeignKey(Reviewer, on_delete = models.CASCADE)
    rev_stars = models.IntegerField()
    num_o_ratings = models.IntegerField()


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)