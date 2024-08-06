import boto3

dynamodb = boto3.resource('dynamodb', 
                          region_name='us-east-1',
                          #aws_access_key_id='AKIA4MTWHWW4ZVPEBXYPGMFH',
    #aws_secret_access_key='bOrcX8ltPNaOHFnlj60Xa8ouge6GutPAVvGiZK7fovZC'
    #aws_session_token='your_session_token'  # Only if using temporary session tokens
    )
table = dynamodb.Table('Books')

resp = table.get_item(Key={"Author": "John Grisham", "Title": "The Rainmaker"})

print(resp['Item'])
