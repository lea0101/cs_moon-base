#
# The aliens seem to be trying to make direct contact, so it's time
# for us to properly listen.
# Write a server that listens on ('localhost', 10000).
# The flag will be sent to that address
# record signal to /tmp/aliensignallog.txt
#
# If you get an address already in use error then try again in a few
# moments.
#


import socket
def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\\n")
    
def writeToFile(msg):
  with open("/tmp/aliensignallog.txt", "w") as myFile:
    myFile.write(msg)


host = 'localhost'
port = 10000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))


while True:
  server.listen(1)
  conn, addr = server.accept()
  try:
    response = conn.recv(1024)
    writeToFile(response.decode())
  except:
    print("Error")
