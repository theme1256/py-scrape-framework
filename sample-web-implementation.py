#!/usr/bin/env python3
# -*- coding: utf8 -*- 
from scraper import Scraper
import pyodbc 
import cgitb
import cgi
import sys
import json



if __name__ == '__main__':
	Scraper = Scraper()
	reply = Scraper.find(url, element)

	# Fetch parameters from URL
	form = cgi.FieldStorage()
	data = form.getvalue("url")
	element = form.getvalue("element")

	# Set JSON header for good measure
	print("Cache-control: no-cache")
	print("Content-Type: application/json; charset=UTF-8")

	# Verify that some input was given
	if url is "" or url is None:
		print(json.dumps({"error": True, "reason": "Missing URL", "msg": "No URL where data should be fetched, was given"}))
	elif element is "" or element is None:
		print(json.dumps({"error": True, "reason": "Missing element", "msg": "No element to search for was given"}))
	else:
		# Handle data from Scraper
		if reply is False:
			print(json.dumps({"error": True, "reason": "Not found", "msg": "The requested element wasn't found"}))
		elif reply is None:
			print(json.dumps({"error": True, "reason": "Communication error", "msg": "RequestException thrown"}))
		elif hasattr(reply, status_code):
			print(json.dumps({"error": True, "reason": "{} status returned".format(reply.status_code), "msg": "Server replied with status code {}".format(reply.status_code)}))
		else:
			print(json.dumps({"error": False, "reason": "object found", "data": reply}))