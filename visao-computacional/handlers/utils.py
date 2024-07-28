import json
import boto3

bedrock = boto3.client('bedrock-runtime')

def generate_pet_tips(pets):
    if not pets:
        return "No pets detected to generate tips."
    
    pet_names = [label['Name'] for label in pets]
    pet_names_str = ', '.join(pet_names)
    
    prompt = f"Me de dicas detalhadas sobre os seguinte(s) pets: {pet_names_str}.responda em portugues e Inclua as seguintes informações: 1. nível de energia e necessidade de exercícios, 2. Temperamento e comportamento, 3. Cuidados e necessidades, 4. Problemas de Saúde Comuns."
    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 3072,
            "stopSequences": [],
            "temperature": 0.7,
            "topP": 0.9
        }
    })

    try:
        print("Bedrock Request Body:", body)
        response = bedrock.invoke_model(
            modelId="amazon.titan-text-premier-v1:0",
            contentType="application/json",
            accept="application/json",
            body=body
        )
        
        response_body = json.loads(response['body'].read().decode('utf-8'))
        print("Bedrock Response Body:", response_body)
        
        if 'results' in response_body and len(response_body['results']) > 0:
            tips = response_body['results'][0].get('outputText', 'Error generating tips.')
        else:
            tips = 'Error generating tips.'
        
        return tips

    except Exception as e:
        print("Error in generate_pet_tips:", e)
        return "Error generating tips."
