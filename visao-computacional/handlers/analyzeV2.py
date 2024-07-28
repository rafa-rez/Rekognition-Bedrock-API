import json
import boto3
import datetime
from handlers.utils import generate_pet_tips

rekognition = boto3.client('rekognition')

def analyze_image_v2(event, context):
    try:
        body = json.loads(event['body'])
        bucket = body['bucket']
        image_name = body['imageName']
        url_to_image = f"https://{bucket}.s3.amazonaws.com/{image_name}"
        
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': image_name}},
            MaxLabels=10,
            MinConfidence=75
        )

        print("Rekognition Response:", json.dumps(response))

        labels = response['Labels']
        pets = [label for label in labels if label['Name'] in ['Animal', 'Dog', 'Pet', 'Cat', 'Labrador']]
        faces = [label for label in labels if label['Name'] == 'Person']

        result_pets = [{
            'labels': [{'Name': label['Name'], 'Confidence': label['Confidence']} for label in pets],
        }]

        tips = generate_pet_tips(pets)
        print("Generated Tips:", tips)

        response_body = {
            'url_to_image': url_to_image,
            'created_image': datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'pets': result_pets if pets else None,
            'faces': faces if faces else None,
            'tips': tips if tips else "No tips available"
        }

        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }

    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
