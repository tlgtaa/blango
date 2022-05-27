import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView

from blango_auth.views import profile
from blango_auth.forms import BlangoRegistrationForm
from blog.views import index, get_my_ip, post_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("post/<slug>/", post_detail, name="blog-post-detail"),
    path('ip/', get_my_ip),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", profile, name="profile"),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("allauth.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
