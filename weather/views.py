import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    urls = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=fd8693717fdb7011ddc4fcb19d74dcd4'
    city = 'Kathmandu'

    r = requests.get(urls.format(city)).json()
    city_weather={
        'city':city,
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
    }
    
    context = {'city_weather':city_weather}
    return render(request,'weather/weather.html',context)
