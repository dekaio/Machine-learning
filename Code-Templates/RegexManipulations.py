import re

def get_sci_timestamp_parse(string):
    timestamp_reg = r'^([A-Za-z]{3}\s[0-9]{2}\s[0-9]{2}\:[0-9]{2}\:[0-9]{2})'
    event_reg = r'^(\w+\:){2}\w+\s(\w+\:\w+)'
    event_reg = r'\[([0-9]{3})\](.*)'
    if re.search(timestamp_reg, string):
        timestamp = re.search(timestamp_reg, string)
        return timestamp.group()
    else:
        return 0
