import requests
from .models import City
from django.shortcuts import render, redirect
from .forms import CityForm

# Create your views here.
def index(request):
    urls = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=fd8693717fdb7011ddc4fcb19d74dcd4'
    err_msg = ''
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name = new_city).count()
            
            if existing_city_count == 0:
                r = requests.get(urls.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City doesnot exists!'
            else:
                err_msg = 'City already added!'


    form = CityForm()

    cities = City.objects.all()

    weather_data = []
    for city in cities:

        r = requests.get(urls.format(city)).json()
        city_weather = {
            'city':city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    
    context = {'weather_data':weather_data,'form':form,'err_msg':err_msg}
    return render(request,'weather/weather.html',context)


def delete_city(request, city_name):
    City.objects.get(name = city_name).delete()
    return redirect('home')
