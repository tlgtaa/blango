import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from blog import views

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("post/<slug>/", views.post_detail, name="blog-post-detail"),
    path('ip/', views.get_my_ip),
]


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
