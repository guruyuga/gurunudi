#!/usr/bin/env python

"""
List of APIs supported by Gurunudi
"""
API_CHAT		='chatbot' #real time conversation and knowledge q&a - ideal for chatbots

"""
Fields returned in response JSON by Gurunudi API calls and Fields sent in request JSON to Gurunudi API calls
"""
FIELD_LANG='lang'
FIELD_TARGET_LANG='target'
FIELD_CONTEXT='context'
FIELD_TEXT="text"
FIELD_ERROR="error"
FIELD_LIST="list"
FIELD_MODEL="model"

ERROR_SERVER_INACCESSIBLE="server_inaccessible"
ERROR_INVALID_LANGUAGE_CODE="invalid_language_code" 
ERROR_NO_RESPONSE="no_response_for_api"
