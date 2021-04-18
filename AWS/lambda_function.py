import botocore.vendored.requests as requests
import json
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('infrastructure')

def criainfra(quantity):
    response=table.get_item(Key={'quantity': quantity})
    if 'Item' in response:
        url="http://ec2-54-83-78-115.compute-1.amazonaws.com:8080/generic-webhook-trigger/invoke"
        r = requests.post(url, headers = {"token": "11988b8a261c396da3d61dc5b7db928ffd"})
        return{'fulfillmentText' : response['Item']['resource']}
    else:
        return{'fulfillmentText' : 'Procure o time de DevOps'}

def lambda_handler(event, context):
  quantity=event['queryResult']['parameters']['quantidade']
  return criainfra(int(quantity))