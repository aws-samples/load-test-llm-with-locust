
from locust import User, task, between
import logging

import boto3
import json

# Create a Boto3 client for Bedrock Runtime
bedrock_client = boto3.client(service_name='bedrock-runtime')

max_tokens_to_sample = 200

# Define the prompt and other parameters
prompt = f"""\n\nHuman: 
Write a long and high-quality story about two dogs. Make the story longer than {max_tokens_to_sample}

Rex and Charlie were best friends who did everything together. They lived next door to each other with their human families and spent all day playing in the backyard. Rex was a golden retriever, always happy and eager for fun. Charlie was a German shepherd, more serious but very loyal. 

Every morning, Rex and Charlie would wake up and bark excitedly, ready to start the day's adventures. Their families would let them out into the backyard and they'd run around chasing each other and sniffing for interesting smells. After tiring themselves out, they'd nap in the shade of the big oak tree, Rex's tail still thumping contentedly even in his sleep. 

\n\nAssistant:"""



modelId = 'anthropic.claude-v2'
accept = 'application/json'
contentType = 'application/json'

body = json.dumps({
    "prompt": prompt,
    # specify the parameters as needed
    "max_tokens_to_sample": max_tokens_to_sample,
    "temperature": 0.1,
    "top_p": 0.9,
})

class LLMUser(User):
    @task
    def generation(self):
        # Invoke the model
        with self.environment.events.request.measure("[Send]", "Prompt"):
            response = bedrock_client.invoke_model(
                modelId=modelId,
                accept=accept,
                contentType=contentType,
                body=body
            )
            # Process the response
            response_body = json.loads(response.get('body').read())
            logging.info(response_body.get('completion'))
            
        logging.info("Finished generation!")            
