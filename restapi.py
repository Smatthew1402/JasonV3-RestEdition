import requests
import json as js

class RESTBike:
    
    def __init__(self, colours = "" ,loc:str = "IP", dist:int = 10):
        self.URL = "https://bikeIndex.org:443/api/v3/search?page=1&per_page=25&"+ colours +"&location=" + loc + "&distance=" + str(dist) + "&stolenness=proximity"
        self.response = requests.get(self.URL)
        self.data = self.processURL()['bikes']
        self.userin={'color':colours, 'Location':loc, 'distance':dist}
        self.numpictures = 0
        self.bikesWPictures = []
        

    def processURL(self):
        return js.loads(self.response.text)

    def searchpictures(self):
        for bike in self.data:
            if bike["thumb"]:
                self.numpictures +=1
                self.bikesWPictures.append(bike)

    def rundemo():
        color = input("Please enter a color:\n")
        location = input("Please enter a location:\n")
        distance = int(input("Distance from the location:\n"))
        demoRestbike = RESTBike(color, location, distance)
        demoRestbike.run()
        write = input("write bikes with pictures to picturebikes.json? Yes/No:")
        if write == 'Yes':
            demoRestbike.dumpbikes("picturebikes.json", demoRestbike.bikesWPictures)
        

    def run(self):
        print("Getting "+str(self.userin['color'])+ " bikes stolen within " + str(self.userin['distance']) + " of " +str(self.userin['Location'])+"\n")
        print(str(len(self.data)) + " Bikes found: searching for Photos\n")
        self.searchpictures()
        print(str(self.numpictures) + " Bikes with pictures within area")

    def dumpbikes(self, filename:str, data):
        with open(filename, 'w') as json:
            js.dump(data, json, indent = "  ", ensure_ascii=False)


if __name__ == "__main__":
    rst= RESTBike("blue", dist=15)
    rst.searchpictures()
    RESTBike.rundemo()
    


