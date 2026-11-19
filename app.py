pip install openai
pip install azure-ai-ml
python -m pip install azure-identity

from openai import AzureOpenAI
endpoint = "https://project6254556-resource.services.ai.azure.com/api/projects/project625245788"
api_key = "jfdfdsnjsjkaksndjnasjkdklasmadsnjkasndklasmldasnhasujckasmmasdn;salkas"
deployment_name = "gpt-5-mini"
from openai import OpenAI

client = OpenAI(
    api_key=api_key,
    base_url=f"{endpoint.rstrip('/')}/openai/v1/"
)

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "What is the capital of India?"}
    ]
)

print(response.choices[0].message.content)
