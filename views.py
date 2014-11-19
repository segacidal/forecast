from django.shortcuts import render

from utils.forecast import Forecast

from collections import defaultdict
import json

def index(request):

    data = defaultdict(dict)

    cities = ('Houston', 'Bogota')
    
    for city in cities:
        f = Forecast(city)
        data[city]['Temp(F)'] = f.get_temp()
        data[city]['Temp(C)'] = f.get_temp('C')
        data[city]['Humidity'] = f.get_humidity()
        data[city]['Summary'] = f.get_summary()

    return render(request, 'forecast/index.html', {'data': dict(data)})
