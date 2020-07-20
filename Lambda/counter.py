import json
import os
import boto3

#print("heres your shit:")
#os.environ['TABLE_NAME'] = 'testing'
#print(os.environ["TABLE_NAME"])
    
def lambda_handler(event,context):  #event, context
    table_name = os.environ["TABLE_NAME"]
    table = boto3.resource("dynamodb").Table(table_name)
    
    response = table.update_item(
        Key={
            'id': 'Count'
        },
        #UpdateExpression="set Amount = Amount + :inc", 
        UpdateExpression='ADD Amount :inc',  
        ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues="UPDATED_NEW"
    )
    # response is equal to the DB Count+1 
    
    # turn response into a variable
    responseBody = json.dumps({"visitorCount": int(float(response["Attributes"]["Amount"]))})
    
     
    apiResponse = {
    "isBase64Encoded": False,
    "statusCode": 200,
    "body": responseBody,
    "headers": {
        "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,OPTIONS" 
        },
    }

    # Return api response object
    return apiResponse
