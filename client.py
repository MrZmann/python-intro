# TODO: 
# implement the client
# It should send each element of integers_to_send to
# the server, one at a time. You will have to encode 
# the data using utf-8 (see comment)
#
# After sending one element, the server will immediately 
# send back a response. Please print out the response.
#

import socket

# Define the server address (localhost and port 65432)
server_address = ('localhost', 65432)

# Define the array of integers
integers_to_send = ['1', '2', '3', '4', '5', '999']

# Implement the following pseudocode
# Check out server.py to help you out
# with _ as _:
    # Connect to server
    # For each i in integers_to_send
        # send i.encode('utf-8') to the server
        # get a response from the server and decode it using .decode('utf-8')
        # print the response

