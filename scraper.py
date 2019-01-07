#!/usr/bin/env python3
# -*- coding: utf8 -*- 
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re

class Scraper():
	debug = False
	verbose = False

	# Simple parsing of debug and verbose params
	def __init__(self, debug = False, verbose = False):
		self.debug = debug
		self.verbose = verbose

	# Simple method that prints if in debug mode
	def out(self, m, force = False):
		if self.debug or force:
			print(m)

	# Simple method that prints if in vebose debug mode
	def logging(self, m):
		if self.verbose and self.debug:
			print(m)

	# Method used to parse the HTML and return one or more elements that matches the query
	def parse(self, soup, elem):
		# parse "elem" into an element, an id and a list of classes
		elm_classes = elem.split(".")
		tmp = elm_classes[0].split("#")
		elm = tmp[0]
		elm_id = ""
		if len(tmp) > 1:
			elm_id = tmp[1]
		elm_classes.remove(elm_classes[0])
		self.out("Looking for an element of type: {}, with ID: \"{}\" with {} class(es)".format(elm, elm_id, len(elm_classes)))
		self.logging("Classes: {}".format(elm_classes))

		# Counting elements
		elm_count = len(soup.find_all(elm))
		self.out("Found {} elements marked with \"{}\"".format(elm_count, elm))

		elms = soup.select(elem)
		elms_count = len(elms)
		self.out("Found {} elements matching that query:".format(elms_count))
		if elms_count == 0:
			return False
		if elms_count == 1:
			return elms[0]
		else:
			return elms

	# The methoad that one should use when using this class
	def find(self, url, elem):
		# Load the file
		soup = self.load(url)

		if soup is None:
			return None
		elif hasattr(soup, status_code):
			return soup

		if ">" in elem:
			levels = elem.split(">")
			prev = soup
			for item in levels:
				prev = self.parse(prev, item)
			self.out(prev)
			return prev
		else:
			out = self.parse(soup, elem)
			self.out(out)
			return out

	# Used to fetch the content of a site
	def load(self, url):
		if "http" in url:
			try:
				with closing(get(url, stream=True)) as resp:
					if self.is_good_response(resp):
						raw_html = resp.content
					else:
						self.out('Error during requests to {}, responded with: {}'.format(url, resp.status_code), True)
						return resp

			except RequestException as e:
				self.out('Error during requests to {} : {}'.format(url, str(e)), True)
				return None
		else:
			raw_html = open(url).read()
		soup = BeautifulSoup(raw_html, 'html.parser')
		self.out("Loaded {}".format(url))
		self.logging("Loaded:\n{}\nFrom: {}".format(soup.prettify(), url))
		return soup

	# Used to verify that the fetched content didn't fail
	def is_good_response(self, resp):
		"""
		Returns True if the response seems to be HTML, False otherwise.
		"""
		content_type = resp.headers['Content-Type'].lower()
		return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)