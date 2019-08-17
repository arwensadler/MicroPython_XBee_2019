""" Code for the TRANSMITTING module. Sends out a signal every 100 ms
to the receiving module.

It works by checking if the amount of time between transmissions has elapsed,
and then sending a signal to the coordinator XBee. Print statement is
included after the sending line for debugging/timing the number of
transmissions.

@arwensadler
"""

import xbee
import time

# How often to send a signal in ms
interval = 100
# Initialize last_sent to the current time
last_sent = time.ticks_ms()

# Start looping through
while True:
    # Check if it's time to send a signal
    if time.ticks_diff(time.ticks_ms(), last_sent) > interval:
        # Attempt to send a signal
        try:
            xbee.transmit(xbee.ADDR_COORDINATOR, "h") # Arbitrary message content
            print("sent!")
        except Exception as err:
            print(err)
        # Reset last_sent to the current time
        last_sent = time.ticks_ms()
