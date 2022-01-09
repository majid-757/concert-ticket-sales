from django.urls import path

from .views import LoginView, LogoutView, ProfileView, ProfileRegisterView, ProfileEditView


urlpatterns = [
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView),
    path('profile/', ProfileView),
    path('profileRegister/', ProfileRegisterView),
    path('profileEdit/', ProfileEditView),
]


