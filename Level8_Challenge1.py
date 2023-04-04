
# Connect over TCP to the following server 'localhost', 10000
# Initiate communication with GET to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#
import socket

HOST = 'localhost'
PORT = 10000
BUFFER_SIZE = 4096
TIMEOUT = 5

msg1 = b"GET"

def decrypt(message):
    possibleList = []
    for i in range(1, 27):
        string = ''
        for char in message:
            shiftNum = i
            if ord(char) in range(65, 91):
                if ord(char) + shiftNum not in range(65, 91):
                    shiftNum -= 26
                string += chr(ord(char) + shiftNum)
            else:
                string += char
        possibleList.append(string)
    return possibleList


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(TIMEOUT)
s.connect((HOST, PORT))
s.send(msg1)
data = s.recv(BUFFER_SIZE)

d = data.decode("utf-8")
sentences = d.split("\n")

print(sentences)
answers =[]
wordlist = [" LAMP ", " GARDEN ", " SULTAN ", " HIM ", " WOMAN ", " RING "," BRASS ", " JEWELS ", " PALACE ", " MAGIC ", " ALADDIN ", " WONDERFUL ", " GENIE ", " THE ", " SLAVE ", " THY ", " MASTER "]
for i in range(1,4):
    for x in decrypt(sentences[i]):
        for a in wordlist:
            if a in x:
                answers.append(x)
                break 

print("ANSWERS BELOW:")
print(answers)
if len(answers)==3:
    message = answers[0] +"\n" + answers[1] +"\n" + answers[2]
    print("Sending: " + message)
    s.send(bytes(message,'utf-8'))
else:
    print("Not enough answers to send.")
flag = s.recv(BUFFER_SIZE)
print(flag)
