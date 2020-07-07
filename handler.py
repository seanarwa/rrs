import os
import json

def root(event, context):

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True
    }

    body = {
        "name": os.environ['NAME'],
        "version": os.environ['VERSION']
    }

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps(body)
    }
