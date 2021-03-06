#!/usr/bin/python
import subprocess
import os
import sys

fileName = "/tmp/output.iq"
actualFile = "output.iq"

fileToWriteTo = open(actualFile, 'wb')
with open(sys.argv[1]) as fp:
  for line in fp:
    args = line.rstrip().split(" ")
    print("args: ", args)
    message = subprocess.check_output(["python", "generate_message.py"] + args[0:-1]).rstrip()
    print("Message: " + str(message))
    ignore = subprocess.check_output(["python3", "encode_wavebird.py", message, fileName, args[-1]])
    print("Ignore: " + str(ignore))
    with open(fileName, 'rb') as tempFile:
      fileToWriteTo.write(tempFile.read())
    os.remove(fileName)



