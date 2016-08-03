# coding=utf8
#
# This is a function to convert a datetime to another timezone
#
# Author: Dinesh Patra <dineshpatra28@gmail.com>
#
# Python Version: 2.7

import pytz, datetime, tzlocal


def get_target_datetime_obj(source_datetime_str, source_datetime_format, source_timezone, target_timezone):
    """
    # | Function to convert a given datetime  in one timezone to another timezone
    # |
    # | Arguments:
    # |     <source_datetime_str>:    Source datetime in string
    # |     <source_datetime_format>: Source datetime is in which formatLike "%Y-%m-%d"
    # |     <source_timezone>:        From which timezone. It should be one of the pytz timezone
    # |     <target_timezone>:        To which timezone. It should be one of the pytz timezone
    # |
    # | Returns datetime object
    """
    system_offset_str = pytz.timezone(str(tzlocal.get_localzone())).localize(datetime.datetime.now()).strftime('%z')
    source_offset_str = pytz.timezone(str(source_timezone)).localize(datetime.datetime.now()).strftime('%z')
    target_offset_str = pytz.timezone(str(target_timezone)).localize(datetime.datetime.now()).strftime('%z')

    system_offset_in_min = int(str(system_offset_str[0]) + str(int(system_offset_str[-4:-2])*60 + int(system_offset_str[-2:])))
    target_offset_in_min = int(str(target_offset_str[0]) + str(int(target_offset_str[-4:-2])*60 + int(target_offset_str[-2:])))
    source_offset_in_min = int(str(source_offset_str[0]) + str(int(source_offset_str[-4:-2])*60 + int(source_offset_str[-2:])))

    source_datetime_obj = datetime.datetime.strptime(source_datetime_str, source_datetime_format)
    system_datetime_obj = source_datetime_obj + datetime.timedelta(minutes=(system_offset_in_min - source_offset_in_min))
    target_detetime_obj = system_datetime_obj + datetime.timedelta(minutes=(target_offset_in_min - system_offset_in_min))
    return target_detetime_obj


# Convert Australia/Melbourne to Asia/Kolkata
# Time in Australia/Melbourne: 2016-08-03 16:25:00
print get_target_datetime_obj("2016-08-03 16:25:00", "%Y-%m-%d %H:%M:%S", 'Australia/Melbourne', 'Asia/Kolkata')

