from django.shortcuts import render

# Create your views here.
def index(request):
    urls = 'api.openweathermap.org/data/2.5/weather?q={}&appid=fd8693717fdb7011ddc4fcb19d74dcd4'
    city = 'Kathmandu'

    r = requests.get(urls.format(city))
    print(r.text)
    return render(request,'weather/weather.html')
