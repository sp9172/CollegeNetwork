"""College URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from unicodedata import name
# from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# from College.Network.views import about, contact
from Network import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="HomePage"),
    path('indexpage',views.Index,name="Firstpage"),
    path('login',views.user_login,name="Login"),
    path('singup',views.singup,name="SingUp"),
    path('userlogout',views.userlogout,name='UserLogout'),
    path('userprofile',views.userprofile,name="UserProfile"),
    path('postadd',views.AddPost,name="AddPost")
    
    # path('about/',views.about,name="Aboutpage"),
    # path('contact/',views.contact,name="ContactPage"),
    
   
    # path('userlogout',views.userlogout,name='UserLogout')
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
