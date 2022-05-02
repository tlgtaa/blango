from django.contrib import admin
from django.urls import path

from blog import views

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("post/<slug>/", views.post_detail, name="blog-post-detail"),
]
