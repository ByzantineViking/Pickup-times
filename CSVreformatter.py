
import pandas

class Formatting(object):
    def __init__(self):
        self.locations = pandas.read_csv("locations.csv")
        self.pickup = pandas.read_csv("pickup_times.csv")

    def returnLocs(self):
        locationList = []
        for location in self.locations["location_id"]:
            locationList.append(str(location))
        return locationList

    def formatPickup(self):
        dateList = []
        timeList = []
        for time in self.pickup["iso_8601_timestamp"]:
            
            #Fishing the date
            def apuT(aika) : 
                found = False
                finished = False
                date = []
                while (not found or not finished):
                    for char in aika:
                        if char == "T" :
                            found = True
                        elif char == "Z" :
                            finished = True
                        elif not found:
                            date.append(char)
                        else:
                            pass
                    finished = True
                return date


            # Fishing the time of the day
            def apuZ(aika):
                found = False
                finished = False
                hours = []
                while (not finished):
                    for char in aika:
                        if char == "T":
                            found = True
                        elif char == "Z":
                            finished = True
                        elif found == True:
                            hours.append(char)
                        else:
                            pass
                    finished = True
                return hours

            dateList.append(apuT(time))
            timeList.append(apuZ(time))
            

        reformattedTime = []
        for time in timeList:
            reformattedTime.append(''.join(time))

        reformattedDate = []
        for date in dateList:
            reformattedDate.append(''.join(date))
        
        locationList = []
        for location in self.pickup["location_id"]:
            locationList.append(str(location))

        pickupList = []
        for pickup in self.pickup["pickup_time"]:
            pickupList.append(str(pickup))

        final = list(zip(locationList, reformattedDate, reformattedTime, pickupList))
        
        return final

    

    def formatLocations(self):
        
        locationList = []
        for location in self.locations["location_id"]:
            locationList.append(str(location))

        longitudeList = []
        for longitude in self.locations["longitude"]:
            longitudeList.append(float(longitude))

        latitudeList = []
        for latitude in self.locations["latitude"]:
            latitudeList.append(float(latitude))
        
        final = list(zip(self.returnLocs(), longitudeList, latitudeList))
        
        return final


