from logging import error
from multiprocessing import context
from django.shortcuts import render
import json
import urllib.request
import urllib.error
# Create your views here.


def index(request):
    if request.method == 'POST':
        
        city = request.POST['city']
        try:
            res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=77aa9f064ee96010bb938e5385444bd6').read()
        except urllib.error.HTTPError as err:
            context = 'resource not found'+ " "+ str(err.code)
            return render(request, 'index.html', {'context':context})

        
        json_data = json.loads(res)
        data = {
            'country_code':str(json_data['sys']['country']),
            'coordinate':str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            'temp':str(json_data['main']['temp']) + 'k',
            'pressure':str(json_data['main']['pressure']),
            'humidity':str(json_data['main']['humidity']),
        }
    
    else:
       data = {}
       city = ''
    return render(request, 'index.html', {'city': city, 'data': data})