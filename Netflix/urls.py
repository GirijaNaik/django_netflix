from Netflix.views import Home, ProfileList, ProfileCreate, Watch, ShowMovieDetail, ShowMovie
from django.urls import path
from .api import UserAPI, RegisterAPI, LoginAPI, LogoutAPI,  MovieCreateAPI, MovieViewAPI, Upcoming_moviesAPI, Upcoming_moviesViewAPI, Top_rated_movieAPI, Top_rated_movieViewAPI
from .api import comedy_moviesViewAPI,  romantic_moviesViewAPI, action_moviesViewAPI, horror_moviesViewAPI, kids_moviesViewAPI

app_name = 'Netflix'

urlpatterns = [
    path('', Home.as_view()),
    path('user/', UserAPI.as_view()),
    path('api/register/', RegisterAPI.as_view()),
    path('api/login/', LoginAPI.as_view()),
    path('api/logout/', LogoutAPI.as_view()),
    path('movies/', MovieViewAPI.as_view()),
    path('Upcoming_movies/', Upcoming_moviesViewAPI.as_view()),
    path('Top_rated/', Top_rated_movieViewAPI.as_view()),
    path('comedy_movies/', comedy_moviesViewAPI.as_view()),
    path('romantic_movies/', romantic_moviesViewAPI.as_view()),
    path('action_movies/', action_moviesViewAPI.as_view()),
    path('horror_movies/', horror_moviesViewAPI.as_view()),
    path('kids_movies/', kids_moviesViewAPI.as_view()),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/', Watch.as_view(), name='watch'),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name='show_det'),
    path('movie/play/<str:movie_id>/', ShowMovie.as_view(), name='play')
]
