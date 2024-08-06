import boto3
from boto3.dynamodb.conditions import Key

# boto3 is the AWS SDK library for Python.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1',
                          #aws_access_key_id='AKIA4MTWHWW4ZVPEBXYPGMFH',
    #aws_secret_access_key='bOrcX8ltPNaOHFnlj60Xa8ouge6GutPAVvGiZK7fovZC'
    #aws_session_token='your_session_token'  # Only if using temporary session tokens
    )
table = dynamodb.Table('Books')

# When making a Query API call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
# We're using the Key object from the Boto3 library to specify that we want the attribute name ("Author")
# to equal "John Grisham" by using the ".eq()" method.
resp = table.query(KeyConditionExpression=Key('Author').eq('John Grisham'))

print("The query returned the following items:")
for item in resp['Items']:
    print(item)
