from django.shortcuts import render
from .models import Slider3, team   
from youtubers.models import youtuber
# Create your views here.

def home(req):
    sliders = Slider3.objects.all()
    teams =  team.objects.all()
    featured_yts = youtuber.objects.order_by("-created_date").filter(is_featured=True)
    allyts = youtuber.objects.all()
    data = {
        'sliders':sliders, 
        'teams' : teams,
        'featured_yts' : featured_yts,
        'allyts':allyts
    }

    return render(req, 'webpages/home.html', data)

def contact(req):
    return render(req, 'webpages/contact.html')

def services(req):
    return render(req, 'webpages/services.html')

def about(req):
    return render(req, 'webpages/about.html')