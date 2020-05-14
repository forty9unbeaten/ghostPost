from django.urls import path
from ghost_post import views

url_paths = [
    path('', views.landing_view, name='home_landing'),
    path('<str:post_filter>/', views.homepage_view, name='homepage'),
    path('<str:post_filter>/<str:action>/<int:post_id>', views.post_vote_view)
]
