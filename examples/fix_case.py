#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** FIX CASE ************************************/
#  
#  This example shows how to query Gurunudi to fix cases and get true cased text
#  
#***************************** TRUE CASE ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.fix_case("i went to jaPan")
print(response)

#if language other than English, then specify
response = ai.fix_case("emmanuel macron est le président de LA France",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for Case Fixing to generate True Case text visit https://guruyuga.com/languages/
