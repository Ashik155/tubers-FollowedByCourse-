from django.shortcuts import get_object_or_404, render
from .models import youtuber

# Create your views here.

def search(request):

   tubers  = youtuber.objects.order_by("-created_date")
   cities = youtuber.objects.values_list('city', flat=True).distinct()
   cameras = youtuber.objects.values_list('camera_type', flat=True).distinct()
   catos = youtuber.objects.values_list('category', flat=True).distinct()
   
   print("entering into if")

   if 'keyword' in request.GET:
       print("passed if")
       term = request.GET['keyword']
       
       if term:
           tubers = tubers.filter(desc__icontains=term)
    
   if 'city' in request.GET:
       city = request.GET['city']
       print("city is ", city)
       if city:
           tubers = tubers.filter(city__iexact=city)
           print(tubers)

    
   if 'camera_type' in request.GET:
       camera_type = request.GET['camera_type']
       if camera_type:
           tubers = tubers.filter(camera_type__iexact=camera_type)

   if 'category' in request.GET:
       category = request.GET['category']
       if category:
           tubers =  tubers.filter(category__iexact=category)


   data = {
       'tubers': tubers,
       'cities' : cities,
       'cameras':cameras,
       'catos':catos
   }
   return render(request, 'youtubers/search.html', data)


def youtubers(req):
    youtubers = youtuber.objects.all()    
    data ={
        'youtubers' : youtubers
    }
    return render(req, 'youtubers/youtubers.html', data)

def youtubers_details(req,id):
    tuber = get_object_or_404(youtuber,pk=id)
    data = {
        'tuber' : tuber
    }
    return  render(req, 'youtubers/youtubers_details.html', data)
