
from locust import User, task, between
import logging

import boto3
import json

modelId = 'arn:aws:bedrock:us-east-1:70768******:provisioned-model/nnp8ar503q42'
max_tokens_to_sample = 200

system_message = f"You are a long and high-quality story teller. Make the story longer than {max_tokens_to_sample}"

messages = [
  {"role": "user", "content": """
  Rex and Charlie were best friends who did everything together. 
  They lived next door to each other with their human families and spent all day playing in the backyard. 
  Rex was a golden retriever, always happy and eager for fun. Charlie was a German shepherd, more serious but very loyal.  
  Every morning, Rex and Charlie would wake up and bark excitedly, ready to start the day's adventures. 
  Their families would let them out into the backyard and they'd run around chasing each other and sniffing for interesting smells. 
  After tiring themselves out, they'd nap in the shade of the big oak tree, Rex's tail still thumping contentedly even in his sleep. 
  """
  }
]

# Create a Boto3 client for Bedrock Runtime
bedrock_client = boto3.client(service_name='bedrock-runtime')

# Define the prompt and other parameters
accept = 'application/json'
contentType = 'application/json'


class LLMUser(User):
    @task
    def generation(self):
        # Invoke the model
        with self.environment.events.request.measure("[Send]", "Prompt"):
            # Invoke the model
            response = bedrock_client.invoke_model(
                modelId=modelId,
                accept=accept,
                contentType=contentType,
                body=json.dumps({
                    "anthropic_version": "bedrock-2023-05-31", 
                    "messages": messages, 
                    "system": system_message,    
                    "max_tokens": 300, 
                    "temperature": 0.7, 
                    "top_p": 0.9})
            )


            # Process the response
            response_body = json.loads(response.get('body').read())
            print(response_body['content'][0]['text'])
            
        logging.info("Finished generation!")            
