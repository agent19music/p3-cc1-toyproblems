#!/usr/bin/env python3

def convert_to_24_hour(hour, minute, period):
    # Check period and adjust hour
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
        # Format output and print
    print( f"{hour:02d}{minute:02d} hrs")

