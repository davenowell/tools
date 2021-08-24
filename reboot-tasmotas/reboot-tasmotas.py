#! /usr/bin/python3

import urllib.request

######## Variables #########
###########################

# Define the URL segments for device command
tProtocol = "http://"
tPreIP = "10.20."
tSubnet = "50."
tAffix = "/cm?cmnd="
tCommand = "Restart"    #Attention ! Make sure you have the right command to avoid unwanted 
                        # See https://tasmota.github.io/docs/Commands for commands and 
                        # numerical options 
tSpaceChar = "%20"      # Space character for URL
tOption = "1"           # See documentation for options 

# Define the devices to be rebooted
arrDevices = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20.21,22.23,24,25,26,27,28,29,30,31,32,33]

# Construct the URL minus last number of IP address
tURLPrefix = tProtocol + tPreIP + tSubnet
tURLSuffix = tAffix + tCommand + tSpaceChar + tOption

# User messages and warnings
tInitWarning = "To initialize a reboot of Tasmota devices for subnet " + tSubnet.strip('.') + ",\n" + "select y to contine. Select n to cancel."  
tWelcomeMsg = "***** Welcome to the Tasmota Network Device reboot script *****"

######## Functions #########
###########################

# initPrompt - Prompts the user as to whether they would like to perform device resets

def initPrompt(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        print(reply[0])
        return True
    if reply[0] == 'n':
        print(reply[0])
        return False
    else:
        return initPrompt("Press Y to continue or n to cancel.")

# initReboot - Triggers the device reboots
def initReboot(bTrigger):
  if bTrigger:
    # Begin looping command to Tasmota IP addresses on network
      
      for i in arrDevices:
    
    # Construct URL
       tTarget = ""
       status_code = ""
       tTarget = tURLPrefix + str(i) + tURLSuffix
       print(tTarget)
    
    # open a connection to a URL using urllib2
    # handles exceptions 
    
       req = urllib.request.Request(tTarget)
       try: urllib.request.urlopen(req)
       except urllib.error.URLError as e:
            print(e.reason)
            status_code = "404"
    
    # get the result code and print it
       if status_code != "404": 
        status_code = str(urllib.request.urlopen(req).getcode()) 
        
       if status_code == "200":
        print ("Reboot command successfully sent to device at IP address " + tPreIP + tSubnet + str(i))
        # Increment
        i += 1
       else: 
        print ("IP address " + tPreIP + tSubnet + str(i) + " is not available.")
        # Increment
        i += 1
        continue
  else:
      print ("Device reboot has been cancelled.")
      exit()

def main():
  print(tWelcomeMsg)
  bvar = initPrompt(tInitWarning)
  initReboot(bvar)
  exit()
 
if __name__ == "__main__":
  main()


