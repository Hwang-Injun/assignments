# get the request from browser
request = conn.recv(config['MAX_REQUEST_LEN'])

# parse the first line
first_line = request.split('\n')[0]

# get url
url = first_line.split(' ')[1]