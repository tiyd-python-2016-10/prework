import requests

class Endpoint:
    key = "6a757a30081ebf5e"
    def __init__(self, zipcode):
        self.zipcode = zipcode

    def get(self):
        print("getting", self.url.format(self.key, self.zipcode))
        self.results = self.url.format(self.key, self.zipcode)

class Conditions(Endpoint):
    def __init__(self, zipcode):
        super().__init__(zipcode)
        self.url = "http://api.wunderground.com/api/{}/conditions/q/{}.json" 

    def __str__(self):
        return self.results

class Alerts(Endpoint):
    def __init__(self, zipcode):
        super().__init__(zipcode)
        self.url = "key: {}  zip: {}  this would be a url"

a = Alerts(94021)
a.get()
c = Conditions(27707)
c.get()
print(c)

exit()
url = "http://api.wunderground.com/api/{}/conditions/q/{}.json"
zipcode = "27707"
key = "6a757a30081ebf5e"

def get_stuff():
    url_tot = url.format(key, zipcode)
    print(url_tot)
    r = requests.get(url_tot)
    co = r.json()["current_observation"]["temp_f"]
    return co

ans = get_stuff()
print(ans["temp_f"])







