#!/usr/bin/env python

"""Generic URI of the Gurunudi AI API"""
API_URL = "https://www.gurunudi.com/api/{}/{}/"	

"""Gurunudi AI API accepts and sents JSON content only"""
HEADERS = {'Content-type': 'application/json; charset=utf-8', 'Accept': 'application/json','User-Agent':'Gurunudi Client'}

DEBUG = False
