from __future__ import print_function # Python 2/3 compatibility
from botocore.exceptions import ClientError

from builtins import print

__author__ = 'JAISMENE VERMA'

import boto3
from boto3.dynamodb.conditions import Key, Attr



dynamodb = boto3.resource("dynamodb", region_name='ap-south-1')

table = dynamodb.Table('members')


"""def get_status(m_id):
    try:
        response = table.get_item(
            Key={
                'm_id': m_id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response.get('Item')
    if not item:
        return "Member not found"
    return item.get('m_status')"""
def get_row(name):
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
