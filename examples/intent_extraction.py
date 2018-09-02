#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** INTENT EXTRACTION ************************************/
#  
#  This example shows how to query Gurunudi to get intent of a text
#  
#***************************** INTENT EXTRACTION ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.intent("Larry Page was doing his Phd at Stanford University in 1996.")
print(response)

#if language other than English, then specify
response = ai.intent("Larry Page promovierte 1996 an der Stanford University.",lang.GERMAN)
print(response)

#For the latest updated list of languages supported by Gurunudi for Definitions visit https://gurulaghu.com/languages/
