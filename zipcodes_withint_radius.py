# These 3 variables will store the API url as strings to be concatenated.
# The third variable reads the input file containing the target zip codes and stores it as a list.
urlstr_one = "https://www.zipcodeapi.com/rest/<<YOUR API KEY HERE>>/radius.csv/"
urlstr_two = "/5/mile"
with open('./zip_targets.txt') as f:
	zipstr = f.read().splitlines()

# This is the output file.
zipstrfile = "zipcodes_in_radius.txt"

# Import the modules
import urllib.request
import sys
import time

count = 0

# This block makes requests to the API for each zip code in the list and appends the output to the output file.
# Each request is paused to not overload the server.
while count < len(zipstr):
    url = urlstr_one + zipstr[count] + urlstr_two
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    print(text)
    sys.stdout = open(zipstrfile, 'a+')
    print('Here are the zip codes within a 5 mile radius of ' + zipstr[count])
    print(text)
    count += 1
    time.sleep(.2)
