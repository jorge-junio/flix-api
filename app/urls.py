from django.contrib import admin
from django.urls import path
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroyView
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('actors/', ActorListCreateView.as_view(), name='actor-collection'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(),
         name='actor-resource'),

    path('genres/', GenreListCreateView.as_view(), name='genre-collection'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(),
         name='genre-resource'),

    path('movies/', MovieListCreateView.as_view(), name='movie-collection'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(),
         name='movie-resource')
]
