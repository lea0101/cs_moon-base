#
# There is a directory traversal vulnerability in the
# following page http://127.0.0.1:8082/humantechconfig?file=human.conf
# Write a script which will attempt various levels of directory
# traversal to find the right amount that will give access
# to the root directory. Inside will be a human.conf with the flag.
#
# Note: The script can timeout if this occurs try narrowing
# down your search



import urllib.request as requests
url = "http:/127.0.0.1:8082/humantechconfig?file=human.conf"
req = requests.urlopen(url)
print(req.read())

