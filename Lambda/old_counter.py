import os
import boto3

table_name = os.environ["TABLE_NAME"]
table = boto3.resource("dynamodb").Table(table_name)

def get_request(): 
    items = table.scan()["Items"]
    return items[0]["number_visits"]
    
    
def post_request(): 
    table_data = get_request()
    table_increment = table_data+1
    response = table.update_item(
        Key={
            'visitsNumber': 1
        },
        UpdateExpression="set number_visits=:r",
        ExpressionAttributeValues={
            ':r': table_increment
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
    
        
def lambda_handler(event, context):
    return post_request()