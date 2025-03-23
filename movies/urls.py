from django.urls import path

from . import views


urlpatterns = [
    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('reviews/', views.ReviewCreateView.as_view(), name='review-create'),
    path('rating/', views.AddStarRatingView.as_view(), name='rating-create'),
    path('actors/', views.ActorsListView.as_view(), name='actor-list'),
    path('actors/<int:pk>/', views.ActorsDetailView.as_view(), name='actor-detail'),
]
