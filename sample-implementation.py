#!/usr/bin/env python3
# -*- coding: utf8 -*- 
from scraper import Scraper
import argparse
import sys
import json



# Tiny formatter, allowing for line-break in help-text
class SmartFormatter(argparse.HelpFormatter):
	def _split_lines(self, text, width):
		if text.startswith('R|'):
			return text[2:].splitlines()  
		return argparse.HelpFormatter._split_lines(self, text, width)

# Handle arguments
parser = argparse.ArgumentParser(description='Script for testing Scraper', formatter_class=SmartFormatter)
parser.add_argument('-d', '--debug', help='R|Enabels debugging', required=False, action="store_true")
parser.add_argument('-v', '--verbose', help='R|Increases output, when debug is enabled', required=False, action="store_true")
parser.add_argument('-e', '--element', help='R|Tells the script if it should find another element than the default "title"', required=False, action="store", type=str, default="title")
parser.add_argument('-u', '--url', help='R|Tells the script if it should load another url, other than the default: "http://bettermotherfuckingwebsite.com/"', required=False, action="store", type=str, default="http://bettermotherfuckingwebsite.com/")
args = parser.parse_args()

debug = args.debug
verbose = args.verbose
test = args.test
url = args.testurl
element = args.testelement



if __name__ == '__main__':
	Scraper = Scraper(debug, verbose)
	reply = Scraper.find(url, element)

	# Set JSON header for good measure
	print("Cache-control: no-cache")
	print("Content-Type: application/json; charset=UTF-8")

	# Handle data from Scraper
	if reply is None:
		print(json.dumps({"error": True, "reason": "Communication error", "msg": "RequestException thrown"}))
	elif hasattr(soup, status_code):
		print(json.dumps({"error": True, "reason": "{} status returned".format(reply.status_code), "msg": "Server replied with status code {}".format(reply.status_code)}))
	else:
		print(json.dumps({"error": False, "reason": "object found", "data": reply}))