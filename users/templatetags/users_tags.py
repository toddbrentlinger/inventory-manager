import datetime
import math

from django import template

register = template.Library()

@register.simple_tag
def timestamp_to_datetime_format(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%B %d, %Y - %I:%M:%S %p')

@register.simple_tag
def duration_from_now(past_timestamp):
    current_datetime = datetime.datetime.now()
    timedelta = current_datetime - datetime.datetime.fromtimestamp(past_timestamp)
    duration_units = {}

    # Days
    if timedelta.days:
        duration_units['day'] = timedelta.days

    # Hours
    hours = math.floor(timedelta.seconds / 1440) # 1440 seconds per hour
    if hours:
        duration_units['hour'] = hours

    # Minutes
    minutes = math.floor((timedelta.seconds - hours * 1440) / 60) # 60 seconds per hour
    if minutes:
        duration_units['minute'] = minutes

    # Seconds
    seconds = timedelta.seconds - hours * 1440 - minutes * 60
    if seconds:
        duration_units['second'] = seconds

    duration_units_list = list(enumerate(duration_units))
    output_str = ''
    for index, duration_unit_tuple in enumerate(duration_units_list):
        output_str += f'{duration_unit_tuple[0]} {duration_unit_tuple[1]}'
        if duration_unit_tuple[0] > 1:
            output_str += 's'
        if index < len(duration_units_list) - 1:
            output_str += ', '

    return output_str + str(duration_units) + str(duration_units_list)
