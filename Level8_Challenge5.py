#
# Write a script that makes HTTP requests to the server
# http://127.0.0.1:8082/selfdestruct until the numbers match
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the response and stop your attack
# once you see the flag.
#

import urllib.request as requests

from html.parser import HTMLParser

global nums
class MyHTMLParser(HTMLParser):
  def __init__(self):
    global nums
    HTMLParser.__init__(self)
    nums=[]
    
  def handle_data(self, data):
    if data.isdecimal():
      nums.append(int(data))

# This might time out--just keep running the code and you should get the answer.

while True:
  parser = MyHTMLParser()
  req = requests.urlopen("http://127.0.0.1:8082/selfdestruct")
  response = req.read().decode().replace("\n","").replace(" ","")
  parser.feed(response)
  if nums[0]==nums[1]:
    print(response)
    break
