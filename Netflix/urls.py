from Netflix.views import Home, ProfileList, ProfileCreate,Watch,ShowMovieDetail,ShowMovie
from django.urls import path
from .api import UserAPI, RegisterAPI, LoginAPI, LogoutAPI,  MovieCreateAPI, MovieViewAPI

app_name='Netflix'

urlpatterns = [
    path('', Home.as_view()),
    path('api/', UserAPI.as_view()),
    path('api/register/', RegisterAPI.as_view()),
    path('api/login/', LoginAPI.as_view()),
    path('api/logout/', LogoutAPI.as_view()),
    path('api/movie_view/', MovieViewAPI.as_view()),
    path('api/create/', MovieCreateAPI.as_view()),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/', Watch.as_view(), name='watch'),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name='show_det'),
    path('movie/play/<str:movie_id>/', ShowMovie.as_view(), name='play')
]
