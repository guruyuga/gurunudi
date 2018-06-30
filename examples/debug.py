#!/usr/bin/env python

#************************************************* DEBUG *********************************************/
#  
#  This example shows how to enable the DEBUG mode to view raw request and response data of Gurunudi AI
#  
#************************************************* DEBUG *********************************************/


from gurunudi import AI,api,config

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("apple")

#To see the raw request and response data set the debug flag to true
config.DEBUG=True

#Now do some API call and the raw request and response data will be displayed in the console
print(ai.definition)


#For the latest updated list of languages supported by Gurunudi for definition visit https://gurulaghu.com/languages/
