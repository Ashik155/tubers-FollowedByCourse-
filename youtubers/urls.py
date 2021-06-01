from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [

    path("", views.youtubers, name='youtubers'),
    path("search", views.search, name='search'),
    path('<int:id>', views.youtubers_details , name='youtubers_details')

]