
from django.contrib import admin
from django.urls import path

import authentification.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.login_page, name='login'),
    path('logout/', authentification.views.logout_user, name='logout'),
    path('home/', blog.views.home, name='home'),
 ]
