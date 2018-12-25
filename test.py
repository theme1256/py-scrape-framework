#!/usr/bin/env python3
# -*- coding: utf8 -*- 
from scraper import Scraper
import argparse
import sys



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
parser.add_argument('-t', '--test', help='R|Tells the script what part should be testet now', required=True, action="store", type=str)
parser.add_argument('-e', '--testelement', help='R|Tells the script if it should find another element than the default "title"', required=False, action="store", type=str, default="title")
parser.add_argument('-u', '--testurl', help='R|Tells the script if it should load another url, other than the default: "http://bettermotherfuckingwebsite.com/"', required=False, action="store", type=str, default="http://bettermotherfuckingwebsite.com/")
args = parser.parse_args()

debug = args.debug
verbose = args.verbose
test = args.test

test_file = "test.html"
test_url = args.testurl
test_element = args.testelement


# Verify that the choosen action is an available one
possible_tests = ["find_file", "find_url", "load_file", "load_url"]

if test not in possible_tests:
	print("The requested test is not one of the available:")
	print(possible_tests)
	sys.exit()



if __name__ == '__main__':
	Scraper = Scraper(debug, verbose)
	if test == possible_tests[0]:
		Scraper.find(test_file, test_element)
	elif test == possible_tests[1]:
		Scraper.find(test_url, test_element)
	elif test == possible_tests[2]:
		Scraper.load(test_file)
	elif test == possible_tests[3]:
		Scraper.load(test_url)