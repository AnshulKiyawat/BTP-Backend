"""btp URL Configuration

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
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from api import login
from api import posts
from api import profile
from api import project

api_list = [
    {'url':'login/signup', 'method':login.signUp},
    {'url':'login/login', 'method':login.login},

    {'url':'posts/submitpost', 'method':posts.submit_post},
    {'url':'posts/fetchposts', 'method':posts.fetch_posts},

    {'url':'profile/getprofiledetails', 'method':profile.get_profile_details},
    {'url':'profile/editprofiledetails', 'method':profile.edit_profile_details},

    {'url':'project/createproject', 'method':project.create_project},
    {'url':'project/fetchprojects', 'method':project.fetch_projects},
]


urlpatterns = []
for api in api_list:
    urlpatterns.append(path(api['url'], csrf_exempt(api['method'])))
