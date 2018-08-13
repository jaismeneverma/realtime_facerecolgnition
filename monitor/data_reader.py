
from botocore.exceptions import ClientError

from builtins import print



import boto3
from boto3.dynamodb.conditions import Key, Attr



dynamodb = boto3.resource("dynamodb", region_name='ap-south-1')

table = dynamodb.Table('members')

def search_by_name(name):
    try:
        response = table.scan(
            FilterExpression=Attr('m_name').eq(name)
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(response)
        item = response.get('Items')
    if not item:
        return None
    return item
	
def search_by_status():
	try:
		response = table.scan(
			FilterExpression=Attr('m_status').eq(1)
        )
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print(response)
		item = response.get('Items')
	if not item:
		return None
	return item
