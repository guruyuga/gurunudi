#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** DEFINITIONS ************************************/
#  
#  This example shows how to query Gurunudi to get definitions of a word or noun
#  
#***************************** DEFINITIONS ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API

ai = AI()

#To see the raw request and response data set the debug flag to true
config.DEBUG=True

#Now do some API call and the raw request and response data will be displayed in the console
response = ai.define("Emmanuel Macron")

