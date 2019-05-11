import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a62e73ec21419f0220e808befcd41b85'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'index.html', context)
