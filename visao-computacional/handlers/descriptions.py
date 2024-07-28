import json

def v1_description(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'VISION API Version 1'})
    }

def v2_description(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'VISION API Version 2'})
    }
