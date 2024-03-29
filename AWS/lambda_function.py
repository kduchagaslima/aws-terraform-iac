import botocore.vendored.requests as requests
import json
import boto3
import decimal
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('infrastructure')

def criainfra(quantity):
    response=table.get_item(Key={'quantity': quantity})
    if 'Item' in response:
        if (response['Item']['balance']) < 10:
            url="http://<MY_JENKINS_URL>:8080/generic-webhook-trigger/invoke"
            r = requests.post(url, headers = {"token": "<WEBHOOK_JENKINS_JOB_TOKEN>"})
            table.update_item(Key={'quantity': quantity}, UpdateExpression="SET balance = balance + :i", ExpressionAttributeValues={':i': decimal.Decimal(1)})
            return{'fulfillmentText' : "Sua instancia " + response['Item']['resource'] + " está sendo criada"}
        else:
            return{'fulfillmentText' : 'Escopo do projeto alcançado'}
    else:
        return{'fulfillmentText' : 'Você não tem permissão para criar mais de uma instancia por solicitação'}

def lambda_handler(event, context):
  quantity=event['queryResult']['parameters']['quantidade']
  return criainfra(int(quantity))
