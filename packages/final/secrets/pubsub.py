import json
import os
import datetime
import base64
from google.oauth2 import service_account
from google.cloud import pubsub_v1
import logging
from concurrent import futures
import json
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
import time
import requests

# Create Authentication Credentials
# Credentialsproject_id = "mlops-353417"
# topic_id = "mlops"
# gcp_credentials = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mlops-353417-0d6234ccd6b9.json"
# # Create Publisher Client
# publisher = pubsub_v1.PublisherClient(credentials=gcp_credentials)
# topic_path = publisher.topic_path(project_id, topic_id)

# payload = "https://randomapi.com/api/vwt0b3kz?key=OTPV-9TK0-H21A-BZBV"
# Get a Random Quote
# while (True):
#     response = requests.get("https://randomapi.com/api/1e22ab9199eedb189330d7564f9f5061")
#
# json_response = response.json()
# message = f"{json_response['results']}"
# print(message)
# # message = f"{json_response['result']}"
# # @- {json_response['content']}"
# # Publish the Message
#
# data = base64.b64encode(message.encode("utf-8"))
#
# print(type(data))
# future = publisher.publish( topic_path,data=data )
# # print(f"Published messages to {topic_path} - {future.result()}.")
# # print(f"Published messages to {topic_path}.")
# time.sleep(3)



def push_payload(payload, topic, project):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project, topic)
    json_response = payload.json()
    message = f"{json_response['results']}"
    data = base64.b64encode(message.encode("utf-8"))
    future = publisher.publish(topic_path, data=data)
    print("Pushed message to topic.")
#
#
data = requests.get("https://randomapi.com/api/1e22ab9199eedb189330d7564f9f5061")
#
PUB_SUB_TOPIC = "mlops"
PUB_SUB_PROJECT = "mlops-353417"
PUB_SUB_SUBSCRIPTION = "mlops-sub"

while (True):
    print("===================================")
    payload = {"data": data, "timestamp": time.time()}
    print(f"Sending payload: {payload}.")
    push_payload(data, PUB_SUB_TOPIC, PUB_SUB_PROJECT)
    # consume_payload(PUB_SUB_PROJECT, PUB_SUB_SUBSCRIPTION, process_payload, timeout)
    time.sleep(3)






