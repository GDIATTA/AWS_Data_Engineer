import boto3

client = boto3.client('dynamodb', region_name='us-east-1',
                      #aws_access_key_id='AKIA4MTWHWW4ZVPEBXYPGMFH',
    #aws_secret_access_key='bOrcX8ltPNaOHFnlj60Xa8ouge6GutPAVvGiZK7fovZC'
    #aws_session_token='your_session_token'  # Only if using temporary session tokens
    )

try:
    resp = client.delete_table(
        TableName="Books",
    )
    print("Table deleted successfully!")
except Exception as e:
    print("Error deleting table:")
    print(e)
