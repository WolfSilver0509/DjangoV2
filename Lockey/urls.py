
from django.contrib import admin
from django.urls import path

import authentification.views
import blog.views
from django.contrib.auth.views import  (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', authentification.views.login_page, name='login'),
    # path('logout/', authentification.views.logout_user, name='logout'),
    path('', LoginView.as_view(
            template_name='authentification/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('home/', blog.views.home, name='home'),
    path('signup/', authentification.views.signup_page, name='signup'),

 ]
