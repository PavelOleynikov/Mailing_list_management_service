from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from config import settings
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserProfileView, UserProfileUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
