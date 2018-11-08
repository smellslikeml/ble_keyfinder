#!/usr/bin/env python
import boto3
from operator import itemgetter

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def get_loc():
    table= dynamodb.Table('key_loc')
    itms = table.scan()['Items']
    location = sorted(itms, key=itemgetter('tmstmp'), reverse=True)[0]['loc']
    return location
    
def lambda_handler(event, context):
    intent_name = event['request']['intent']['name']
    if intent_name == "findkeys":
        loc = get_loc()
        message = "Your keys are in the " + loc
    else:
        message = "Unknown"
        
    speechlet = build_speechlet_response("Keys Status", message, "", "true")
    return build_response({}, speechlet)
