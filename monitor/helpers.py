import boto3
import datetime


# Function returns the list of all dates between two specific dates
def getAllDatesBetweenTwoDates(from_date, to_date):
    from_date = from_date.split('-') # start date
    to_date = to_date.split('-') # end date
    # Converting string dates to date datatype using date()11
    start_date = datetime.date(int(from_date[0]), int(from_date[1]), int(from_date[2]))
    end_date = datetime.date(int(to_date[0]), int(to_date[1]), int(to_date[2]))
    delta = end_date - start_date         # timedelta
    dates = [] # will store all dates between from_date and to_date
    print(delta)
    for i in range(delta.days + 1):
        dates.append(str(start_date + datetime.timedelta(i)))
    return dates  # returns a list of all dates as strings


# Function to get time difference
def time_difference(t1, t2):
    list_t1 = t1.split(':')
    list_t2 = t2.split(':')
    if int(list_t2[1]) < int(list_t1[1]):
        list_t2[1] = str(int(list_t2[1])+60)
        list_t2[0] = str(int(list_t2[0])-1)
        hours = str(int(list_t2[0]) - int(list_t1[0]))
        mins = str(int(list_t2[1]) - int(list_t1[1]))
        time_difference = hours+':'+mins
        return time_difference
    else:
        hours = str(int(list_t2[0]) - int(list_t1[0]))
        mins = str(int(list_t2[1]) - int(list_t1[1]))
        time = hours+':'+mins
        return time #returns time difference t2 - t1


# Function to add time
def time_addition(t1, t2):
    list_t1 = t1.split(':')
    list_t2 = t2.split(':')
    if int(list_t2[1]) + int(list_t1[1]) >= 60:
        hours = str(1 + int(list_t1[0]) + int(list_t2[0]))
        mins = str((int(list_t1[1]) + int(list_t2[1])) - 60)
        total_time = hours+':'+mins
        return total_time
    else:
        hours = str(int(list_t1[0]) + int(list_t2[0]))
        mins = str(int(list_t1[1]) + int(list_t2[1]))
        total_time = hours+':'+mins
        return total_time  # returns sum of t1 and t2


# Getting total IN time of a member for a particular date
def get_in_time(m_id,date):
    dynamodb = boto3.resource("dynamodb", region_name='ap-south-1')
    table = dynamodb.Table(m_id)
    responseIN = table.get_item(Key={'date': date,'cam_no': 1})
    responseOUT = table.get_item(Key={'date': date,'cam_no': 0})
    try:
        itemIN = responseIN['Item']
        itemOUT = responseOUT['Item']
        IN_time = itemIN['iotime']
        OUT_time = itemOUT['iotime']
        in_out_Time = []  # NOT Necessary
        total_IN_time = '00:00'
        if len(IN_time)==len(OUT_time):
            for i in range(len(IN_time)):
                total_IN_time = time_addition(total_IN_time, time_difference(IN_time[i], OUT_time[i]))
                in_out_Time.append(IN_time[i]+'-'+OUT_time[i])  # appending inoutList
            return total_IN_time, in_out_Time
        else:
            # print('something is wrong')
            return None, None
    except KeyError as e:
        # print('Item not found !')
        return None, None


