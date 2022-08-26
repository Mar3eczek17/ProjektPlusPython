from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start_game', views.start_game, name='start_game'),
    # path('on_game', views.on_game, name='on_game'),
    path('finish', views.finish, name="finish"),
    path('on_game_get', views.on_game_get, name='on_game_get'),
    path('on_game_post', views.on_game_post, name='on_game_post')
]
