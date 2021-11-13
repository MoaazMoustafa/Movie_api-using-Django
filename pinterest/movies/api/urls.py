from django.urls import path
from django.urls.resolvers import URLPattern
from .views import movie_create, movie_delete, movie_index, movie_update

app_name = 'pinterest'
urlpatterns = [
    path('', movie_index, name='movie_index'),
    path('create', movie_create, name='movie_create'),
    path('delete/<int:pk>', movie_delete, name='movie_delete'),
    path('update/<int:pk>', movie_update, name='movie_update'),
]
