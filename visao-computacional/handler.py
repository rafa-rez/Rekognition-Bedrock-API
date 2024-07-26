import json
import boto3
from datetime import datetime

rekognition = boto3.client('rekognition')

def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_description(event, context):
    body = {
        "message": "VISION api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v2_description(event, context):
    body = {
        "message": "VISION api version 2."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def analyze_image(event, context):
    # Extraindo os dados do corpo da requisição
    body = json.loads(event['body'])
    bucket = body['bucket']
    image_name = body['imageName']
    
    # Montando o URL da imagem
    url_to_image = f"https://{bucket}.s3.amazonaws.com/{image_name}"
    created_image = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    # Analisando a imagem com o Rekognition
    response = rekognition.detect_faces(
        Image={'S3Object': {'Bucket': bucket, 'Name': image_name}},
        Attributes=['ALL']
    )
    
    faces_data = []
    for faceDetail in response['FaceDetails']:
        emotions = faceDetail['Emotions']
        primary_emotion = max(emotions, key=lambda x: x['Confidence'])
        
        face_data = {
            'position': faceDetail['BoundingBox'],
            'classified_emotion': primary_emotion['Type'],
            'classified_emotion_confidence': primary_emotion['Confidence']
        }
        faces_data.append(face_data)
    
    # Preparando o retorno
    result = {
        'url_to_image': url_to_image,
        'created_image': created_image,
        'faces': faces_data
    }
    
    # Logando o resultado no CloudWatch
    print(json.dumps(result))
    
    # Retornando a resposta
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }