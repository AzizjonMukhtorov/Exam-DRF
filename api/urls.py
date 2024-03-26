from django.urls import path
from .views import *


urlpatterns = [
    path('', MovieCreateAPI.as_view()),
    path('movielist/', MovieListAPI.as_view()),
    path('update-movie/<int:pk>/', MovieUpdate.as_view()),
    path('delete-movie/<int:pk>/', MovieDelete.as_view()),
    path('actorcreate', ActorCreateAPI.as_view()),
    path('actorlist/', ActorListAPI.as_view()),
    path('update-actor/<int:pk>/', ActorUpdate.as_view()),
    path('delete-actor/<int:pk>/', ActorDelete.as_view()),
    path('directorcreate', DirectorCreateAPI.as_view()),
    path('directorlist/', DirectorListAPI.as_view()),
    path('update-director/<int:pk>/', DirectorUpdate.as_view()),
    path('delete-director/<int:pk>/', DirectorDelete.as_view()),
    path('genrecreate', GenreCreateAPI.as_view()),
    path('genrelist/', GenreListAPI.as_view()),
    path('update-genre/<int:pk>/', GenreUpdate.as_view()),
    path('delete-genre/<int:pk>/', GenreDelete.as_view()),
    path('reterviewcreate', ReviewerCreateAPI.as_view()),
    path('reterviewlist/', ReviewerListAPI.as_view()),
    path('update-reterview/<int:pk>/', ReviewerUpdate.as_view()),
    path('delete-reterview/<int:pk>/', ReviewerDelete.as_view()),
]
