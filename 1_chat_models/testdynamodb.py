import boto3

# Initialize a boto3 session
boto3_session = boto3.Session(region_name='us-east-1')
dynamodb = boto3_session.resource('dynamodb')

# Reference the table
table = dynamodb.Table('ChatMessages')

# Test putting an item
try:
  table.put_item(
      Item={
          'SessionId': 'test_session',
          'Role': 'System',
          'Content': 'Test message'
      }
  )
  print("Successfully wrote to DynamoDB table.")
except Exception as e:
  print(f"Error writing to DynamoDB table: {e}")