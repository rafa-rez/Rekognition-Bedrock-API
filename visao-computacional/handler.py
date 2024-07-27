import json
import boto3
import datetime

rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')

def health(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Service is running'})
    }

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

def analyze_image_v1(event, context):
    try:
        # Extraindo parâmetros da solicitação
        body = json.loads(event['body'])
        bucket = body['bucket']
        image_name = body['imageName']
        url_to_image = f"https://{bucket}.s3.amazonaws.com/{image_name}"
        
        # Chamando o Rekognition para detectar faces
        response = rekognition.detect_faces(
            Image={'S3Object': {'Bucket': bucket, 'Name': image_name}},
            Attributes=['ALL']
        )

        print(json.dumps(response))  # Logando a resposta

        faces = response['FaceDetails']
        result_faces = [{
            'position': {
                'Height': face['BoundingBox']['Height'],
                'Left': face['BoundingBox']['Left'],
                'Top': face['BoundingBox']['Top'],
                'Width': face['BoundingBox']['Width']
            },
            'classified_emotion': max(face['Emotions'], key=lambda x: x['Confidence'])['Type'],
            'classified_emotion_confidence': max(face['Emotions'], key=lambda x: x['Confidence'])['Confidence']
        } for face in faces]

        if not result_faces:
            result_faces = [{
                'position': {
                    'Height': None,
                    'Left': None,
                    'Top': None,
                    'Width': None
                },
                'classified_emotion': None,
                'classified_emotion_confidence': None
            }]

        response_body = {
            'url_to_image': url_to_image,
            'created_image': datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'faces': result_faces
        }

        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def analyze_image_v2(event, context):
    try:
        # Extraindo parâmetros da solicitação
        body = json.loads(event['body'])
        bucket = body['bucket']
        image_name = body['imageName']
        url_to_image = f"https://{bucket}.s3.amazonaws.com/{image_name}"
        
        # Chamando o Rekognition para detectar labels
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': image_name}},
            MaxLabels=10,
            MinConfidence=75
        )

        print(json.dumps(response))  # Logando a resposta

        labels = response['Labels']
        pets = [label for label in labels if label['Name'] in ['Animal', 'Dog', 'Pet', 'Cat', 'Labrador']]
        faces = [label for label in labels if label['Name'] == 'Person']

        result_pets = [{
            'labels': [{'Name': label['Name'], 'Confidence': label['Confidence']} for label in pets],
        }]

        response_body = {
            'url_to_image': url_to_image,
            'created_image': datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'pets': result_pets if pets else None,
            'faces': faces if faces else None
        }

        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }