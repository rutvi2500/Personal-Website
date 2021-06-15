from django.urls import path
from.import views

urlpatterns = [
    path('',views.homepageview,name="home"),
    path('exp',views.exppageview,name="exp"),
    path('certi',views.certipageview,name="certi"),
    path('project',views.projectpageview,name="project"),
    path('contact',views.contactpageview,name="contact"),
]
