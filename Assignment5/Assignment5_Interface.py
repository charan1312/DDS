#!/usr/bin/python2.7
#
# Assignment3 Interface
# Name: 
#

from pymongo import MongoClient
import os
import re
import codecs
import sys
import json
import math

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
	cityToSearch = cityToSearch.strip()
	out = codecs.open(saveLocation1,'w', encoding='utf-8')
	queryRs = collection.find({'city': re.compile('^' + re.escape(cityToSearch) + '$', re.IGNORECASE)})
	for rs in queryRs:
		line = '{0}${1}${2}${3}'.format(rs['name'].upper(),rs['full_address'].upper().replace("\n",","),rs['city'].upper(),rs['state'].upper())
		out.write(line)
		out.write("\n")
	out.close()
	pass

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
	out = codecs.open(saveLocation2,'w', encoding='utf-8')
	queryRs = collection.find({'categories': {"$in":categoriesToSearch}})
	for rs in queryRs:
		dist = distanceCalculator(rs['latitude'],rs['longitude'],float(myLocation[0]),float(myLocation[1]))
		#print dist
		if dist <= maxDistance :
			#print str(dist) + ' - ' + rs['name']
			out.write(rs['name'].upper())
			out.write('\n')
	out.close()
	pass

def distanceCalculator(lat1,long1,lat2,long2):
	R=3959
	degreeToRadian = math.pi / 180.0
	phi1 = lat1 * degreeToRadian
	phi2 = lat2 * degreeToRadian
	deltaLat = ( lat2 - lat1 ) * degreeToRadian
	deltaLong = ( long2 - long1 ) * degreeToRadian
	a = (math.sin((deltaLat / 2)) * math.sin((deltaLat / 2))) + (math.cos(phi1) * math.cos(phi2) * math.sin((deltaLong / 2)) * math.sin((deltaLong / 2)))
	c = 2 * (math.atan2((math.sqrt(a)) , (math.sqrt(1 - a))))
	d = R * c
	return d