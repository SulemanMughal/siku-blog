
from django.urls import path

# import views
from . import views

urlpatterns = [

    # ? Home Route
    path("", views.index, name="index"),

    # ? Specific Blog Post Details Route
    path("post/<slug:title>/", views.details, name="post_details"),
    # path("post/<int:pk>/", views.details, name="post-detail"),

    # ? Search Blog Posts by Title
    path('search', views.search, name="search"),
]