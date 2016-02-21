#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import xml.dom.minidom
import xml.etree.ElementTree as ET
from pprint import pprint
import datetime

def etOrString(func):
    def func_wrapper(xml):
        if isinstance(xml, str):
            return func(ET.fromstring(xml))
        return func(xml)
    return func_wrapper


def getStop(point):
    url = "http://www.linzag.at/static/XML_STOPFINDER_REQUEST"
    data = { "locationServerActive" : 1,
             "outputFormat" : "json",
             "type_sf" : "any",
             "name_sf" : point}
    return requests.get(url,params=data).json()


def getDepartTimes(stop):
    url = "http://www.linzag.at/static/XML_DM_REQUEST"
    data = { "locationServerActive" : 1,
             "sessionID" : 0,
             "type_dm" : "any",
             "name_dm" : stop}

    stepOneRes = requests.get(url, params=data)
    root = ET.fromstring(stepOneRes.content)
    sessionid1 = root.attrib['sessionID']
    data['sessionID'] = root.attrib['sessionID']
    data['requestID'] = root[1].attrib['requestID']
    data['selectAssignedStops_dm'] = 1
    data['assignedStop_dm'] = "4:Linz Landgutstraße"
    stepTwoRes = requests.get(url, params=data)
    root = ET.fromstring(stepTwoRes.content)
    sessionid2 = root.attrib['sessionID']

    data2 = { "sessionID" : data['sessionID'],
              "requestID" : 1,
              "dmLineSelectionAll" : 1
            }

    stepThreeRes = requests.get(url, params=data2)
    root = ET.fromstring(stepThreeRes.content)
    return root[1][4]


@etOrString
def itdDateTimeToDateTime(itdDateTime):
    itdDate = itdDateTime[0]
    itdTime = itdDateTime[1]
    year = int(itdDate.attrib['year'])
    month = int(itdDate.attrib['month'])
    day = int(itdDate.attrib['day'])
    hour = int(itdTime.attrib['hour'])
    minute = int(itdTime.attrib['minute'])
    return datetime.datetime(year, month, day, hour, minute)


class ServingLine():
    def __init__(self, direction, symbol):
        self.direction = direction
        self.symbol = symbol

    def __repr__(self):
        return self.symbol + " " + self.direction

    def __str__(self):
        return self.symbol + " " + self.direction


class Stop():
    def __init__(self, stopId, name, x, y):
        self.name = name
        self.id = stopId
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id + " " + self.name + " (" + self.x + "," + self.y + ")"


class Departure():
    def __init__(self, stop, servingLine, departDateTime):
        self.stop = stop
        self.servingLine = servingLine
        self.departDateTime = departDateTime

    def __str__(self):
        return self.stop.__str__() + " " + self.servingLine.__str__() + \
                " " + self.departDateTime.__str__()

    def __repr__(self):
        return self.stop.__repr__() + " " + self.servingLine.__repr__() + \
                self.departDateTime.__repr__()


@etOrString
def itdDepartureToDeparture(itdDeparture):
    itdD = itdDeparture
    stop = Stop(itdD.attrib['stopID'], itdD.attrib['stopName'], 
            itdD.attrib['x'], itdD.attrib['y'])
    servingLine = itdServingLineToServingLine(itdD[1])
    departTime = itdDateTimeToDateTime(itdD[0])
    return Departure(stop, servingLine, departTime)


@etOrString
def itdServingLineToServingLine(itdServingLine):
    direction = itdServingLine.attrib['direction']
    symbol = itdServingLine.attrib['symbol']
    return ServingLine(direction, symbol)

@etOrString
def itdDepartureListToDepartureList(data):
    return [ itdDepartureToDeparture(d) for d in data]

     
    


    
if __name__ == "__main__":
    print(itdDepartureListToDepartureList(getDepartTimes("WIFI Linz / Linz AG")))
    
