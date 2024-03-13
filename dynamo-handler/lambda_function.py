import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('crcvisitcounter')

def lambda_handler(event, context):
 response = table.update_item(
      Key={
          'id': '1'
      }, 
      UpdateExpression='SET vcount = if_not_exists(vcount, :start) + :val',  
      ExpressionAttributeValues={
          ':val': 1,
          ':start': 0
      },
      ReturnValues="UPDATED_NEW"
  )
 response = table.get_item(
      Key={
          'id': '1'
      })
 views=response['Item']['vcount']
 # print(views)
 return views