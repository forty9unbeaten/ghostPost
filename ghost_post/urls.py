from django.urls import path
from ghost_post import views

url_paths = [
    path('', views.landing_view, name='home_landing'),
    path('new/', views.new_post_view, name='new_post'),
    path('<str:post_id>', views.post_detail_view, name='details'),
    path('<int:post_id>/<str:action>', views.post_vote_view),
    path('<str:post_filter>/<str:post_sort>',
         views.homepage_view, name='homepage'),
]
