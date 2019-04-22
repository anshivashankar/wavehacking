import subprocess
import os

fileName = "/tmp/output.iq"
actualFile = "output.iq"

fileToWriteTo = open(actualFile, 'wb')
with open('test.txt') as fp:
  for line in fp:
    args = line.split(" ")
    message = subprocess.check_output(["python", "generate_message.py"] + args[0:-1])
    message = message.rstrip()
    print("Message: " + message)
    ignore = subprocess.check_output(["python3", "encode_wavebird.py", message, fileName, args[-1].rstrip()])
    print("Ignore: " + ignore)
    with open(fileName, 'rb') as tempFile:
      fileToWriteTo.write(tempFile.read())
    os.remove(fileName)



