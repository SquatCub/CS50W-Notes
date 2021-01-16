from django.urls import path #Importing path library

from . import views #Importing views from root

# This is the path that I can get from the browser
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("greet2/<str:name>", views.greet2, name="greet2"), #str:name receive a string
    path("bran", views.bran, name="bran"),
    path("dan", views.dan, name="dan")
]