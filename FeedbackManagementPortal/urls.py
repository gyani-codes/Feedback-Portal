"""FeedbackManagementPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from feedbackApp import views
urlpatterns = [
    # redirect to admin
    url(r'^admin/', admin.site.urls),

    # home page
    url(r'^$',views.HomePage,name='Home'),

    #if return dashboard for student
    url(r'^dashboard_student/$',views.dashboard_student,name = "dashboard_student"),

    # if reuqest for teacher return dashboard of teacher
    url(r'^dashboard_teacher/$',views.dashboard_teacher,name = "dashboard_teacher"),

    # feedback form
    url(r'^form/$',views.feedback_form,name = "feedback_form"),

    # logout
    url(r'^logout/$', views.logout_view,name='logout'),
    
    # teahcer detail
    url(r'^teacher/$', views.teachers_detail, name='teachers_detail'),

    # techer detail in student dashboard , slug is fac code for teacher
    url(r'^teacher/(?P<slug>[-\w\d]+)$', views.teachers_detail2, name='teachers_detail2'),

    # techer detail in teacher dashboard , slug is fac code for teacher

    url(r'^teacher2/(?P<slug>[-\w\d]+)$', views.teachers_detail3, name='teachers_detail3'),

    # feedback detail in student dashboard 

    url(r'^view_feedback/$', views.view_feedback, name='view_feedback'),

    # feedback detail in student dashboard 

    url(r'^view_feedback2/$', views.view_feedback2, name='view_feedback2'),
]
