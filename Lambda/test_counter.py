from moto import mock_dynamodb2
import boto3
import os
import unittest

def aws_credentials():
    #Mocked AWS Credentials for moto
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    os.environ['TABLE_NAME'] = 'testing'

@mock_dynamodb2
class TestLambdaDDB(unittest.TestCase):
    def test_handler(self):
        from counter import lambda_handler
        # Create dynamodb boto3 object
        dynamodb = boto3.client('dynamodb')
        # Get dynamodb table name from env
        ddbTableName = os.environ['TABLE_NAME']
    
        # Create mock table
        dynamodb.create_table(   #took away table= from front 
          TableName = ddbTableName,
          BillingMode='PAY_PER_REQUEST',
          AttributeDefinitions=[
              {
                'AttributeName': 'id',
                'AttributeType': 'S'
              },
        ],
          KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
          ]
        )
       
        LambdaResponse = lambda_handler(0,0)
        print("Lambda response: ", LambdaResponse)
        self.assertEqual(200, LambdaResponse['statusCode'])
    

if __name__ == '__main__':
  aws_credentials()
  unittest.main()
  
  
