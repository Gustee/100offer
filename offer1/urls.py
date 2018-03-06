"""offer1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

import basic.views as bv
import user.views as uv
import job.views as jv
import resume.views as rv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', bv.index),
    path('',bv.index),
    path('test/', bv.test),
    path('login_in/',uv.login_in),
    path('sign_up/',uv.sign_up),
    path('login/',uv.login),
    path('mailconfirmation/',uv.mailConfirmation),
    path('jobs/',jv.jobs),
    path('details/',jv.details),
    path('personal_info/',uv.personal_info),
    path('account/',uv.account),
    path('career_info/',uv.career_info),
    path('experience/',uv.experience),
    path('resume/basic/',rv.basic),
    path('signin/',uv.signin),
    path('signup/',uv.signup)
]

