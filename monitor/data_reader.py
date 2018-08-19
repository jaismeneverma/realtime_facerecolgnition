
from botocore.exceptions import ClientError
from builtins import print
from monitor.helpers import get_in_time, getAllDatesBetweenTwoDates
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
        return None
    else:
        print(response)
        item = response.get('Items')
    if not item:
        return None
        # To convert dictionaries to list
    list_of_item = []
    for dict in item:
        list_of_item.append([dict['m_id'], dict['m_enroll'], dict['m_name'], dict['m_sem'], dict['m_status'], dict['m_date']])
    return list_of_item


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
    # To convert dictionaries to list
    list_of_item = []
    for dict in item:
        list_of_item.append([dict['m_id'], dict['m_enroll'], dict['m_name'], dict['m_sem'], dict['m_status'], dict['m_date']])
    return list_of_item


# To query total IN time of a member between two specific dates
def get_in_time_between_dates(m_id, from_date, to_date):
    dates = getAllDatesBetweenTwoDates(from_date, to_date)
    datewise_total_in_time = []
    datewise_inout_time_list = []
    remove_dates = []  # stores that dates on which no record is found
    for date in dates:
        InTime, InOutList = get_in_time(m_id,date)
        if not InTime or not InOutList:
            remove_dates.append(date)
        else:
            datewise_total_in_time.append(InTime)
            datewise_inout_time_list.append(InOutList)
    for date in remove_dates:  # remove dates which have no records
        dates.remove(date)
    return dates, datewise_total_in_time, datewise_inout_time_list

