"""level5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basicapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/',views.registration,name='registration'),
    path('admin/', admin.site.urls),
    path('newsfeed/',views.newsfeed,name='newsfeed'),
    path('newsfeed/<int:id>/',views.comments,name='comment_post'),
    path('login/',views.user_login,name='login'),
    path('add_post/',views.add_post,name='add_post'),
    path('profiles/',views.user_profiles,name='profiles'),
    path('profiles/<int:user_id>/',views.ind_profile,name='ind_profile'),
    path('follow/<int:id>/',views.add_following,name='follow'),
    path('user_info/',views.user_info,name='user_info'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
