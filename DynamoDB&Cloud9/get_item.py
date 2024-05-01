import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Books')

resp = table.get_item(Key={"Author": "John Grisham", "Title": "The Rainmaker"})

print(resp['Item'])
