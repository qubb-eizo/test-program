from django.urls import path

from account.views import CreateUserAccountView, UserAccountLoginView, UserAccountLogoutView, \
    UserAccountUpdateView, ContactUsView

app_name = 'account'

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='register'),
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', UserAccountLogoutView.as_view(), name='logout'),
    path('profile/', UserAccountUpdateView.as_view(), name='profile'),
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
]
