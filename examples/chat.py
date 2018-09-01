#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** CHAT ************************************/
#  
#  This example shows how to have a general conversation with Gurunudi AI
#  
#***************************** CHAT ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API

ai = AI()

#default language is English
response=ai.chat('who wrote anna karenina?')
print(response)

#if language other than English, then specify
response=ai.chat('qui a écrit anna Karenina?',lang.FRENCH)
print(response)


#For the latest updated list of languages supported by Gurunudi for chat visit https://gurulaghu.com/languages/
