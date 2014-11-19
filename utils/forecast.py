import json
import urllib2
import datetime

class Forecast:
    
    def __init__(self, city='Houston'):
        self.api_key = '3a46d63c104162c8e4673f2081e2c2e8'
        self.lat, self.long = self.get_latlong(city)
        self.time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.city = city
        self.data = self.get_data()

    '''
    Hard-coded for Houston & Bogota right now. In the future will
    look up city's lat/long
    '''
    def get_latlong(self, city):
        if city == 'Houston':
            self.lat = '29.760193'
            self.long = '-95.369390'
        elif city == 'Bogota':
            self.lat = '4.598056'
            self.long = '-74.075833'
        else:
            return 'Error: Could not locate city'
        return (self.lat, self.long)

    def get_data(self):
        self.url = 'https://api.forecast.io/forecast/%s/%s,%s,%s' % (self.api_key, self.lat, self.long, self.time)
        self.json_data = urllib2.urlopen(self.url)
            
        return json.load(self.json_data)

    def get_temp(self, unit='F'):
        temp_F = round(self.data['currently']['temperature'],2)

        if unit == 'C':
            temp_C = round(((temp_F - 32) * 5/9),2)
            return temp_C
        return temp_F

    def get_summary(self):
        return self.data['currently']['summary']

    def get_humidity(self):
        return self.data['currently']['humidity']

if __name__ == '__main__':
    f = Forecast('Bogota') 
    
    print f.get_temp()
