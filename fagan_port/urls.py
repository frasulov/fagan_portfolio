from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="about"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("sendmail", views.sendmail, name="sendmail"),
]