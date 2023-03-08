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
    # A timedelta object between current datetime and datetime using past_timestamp
    timedelta = current_datetime - datetime.datetime.fromtimestamp(past_timestamp)
    # Dictionary keys are string of singular time unit (ex. day, minute, second).
    # Dictionary values are whole number integers of the corresponding time unit.
    duration_units = {}

    # Only add units with non-zero values to duration_units dictionary

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

    # Convert duration_units dictionary to single string
    duration_units_list = list(enumerate(duration_units))
    output_str = ''
    for index, duration_unit_key in duration_units_list:
        output_str += f'{duration_units[duration_unit_key]} {duration_unit_key}'
        if duration_units[duration_unit_key] > 1:
            output_str += 's'
        if index < len(duration_units_list) - 1:
            output_str += ', '

    return output_str
