#!/usr/bin/python2.7
#
# Assignment3 Interface
# Name: Satyam Rohit
#

from pymongo import MongoClient
import os
import sys
import json
import Assignment5_Interface as Assignment5

DATABASE_NAME = "ddsassignment5"
COLLECTION_NAME = "businessCollection"
CITY_TO_SEARCH = "    tempe    "
MAX_DISTANCE = 1
CATEGORIES_TO_SEARCH = ["Fashion", "Food", "Cafes"]
MY_LOCATION = ["33.4294", "-111.9431"] #[LATITUDE, LONGITUDE]
SAVE_LOCATION_1 = "findBusinessBasedOnCity.txt"
SAVE_LOCATION_2 = "findBusinessBasedOnLocation.txt"

def loadBusinessTable(fileName, collection):
    try:
        page = open(fileName, "r")
        parsedJson = json.loads(page.read())
        for oneItem in parsedJson["BusinessRecords"]:
            collection.insert(oneItem)
    except Exception as e:
            print "Error: "+str(e)

if __name__ == '__main__':  
    try:
        #Getting Connection from MongoDB
        conn = MongoClient('mongodb://localhost:27017/')

        #Creating a New DB in MongoDB
        print "Creating database in MongoDB named as " + DATABASE_NAME
        database   = conn[DATABASE_NAME]

        #Creating a collection named businessCollection in MongoDB
        print "Creating a collection in " + DATABASE_NAME + " named as " + COLLECTION_NAME
        collection = database[COLLECTION_NAME]

        #Loading BusinessCollection from a json file to MongoDB
        #print "Loading testData.json file in the " + COLLECTION_NAME + " present inside " + DATABASE_NAME
        #loadBusinessTable("testData.json", collection)
        
        #Finding All Business name and address(full_address, city and state) present in CITY_TO_SEARCH
        #print "Executing FindBusinessBasedOnCity function"
        #Assignment5.FindBusinessBasedOnCity(CITY_TO_SEARCH, SAVE_LOCATION_1, collection)
        dist = Assignment5.distanceCalculator(33.362760000000002,-111.93534,33.423605,-111.939553)
        print dist
        #Finding All Business name and address(full_address, city and state) present in radius of MY_LOCATION for CATEGORIES_TO_SEARCH
        #print "Executing FindBusinessBasedOnLocation function"
        #Assignment5.FindBusinessBasedOnLocation(CATEGORIES_TO_SEARCH, MY_LOCATION, MAX_DISTANCE, SAVE_LOCATION_2, collection)

    except Exception as detail:
        print "Something bad has happened!!! This is the error ==> ", detail
