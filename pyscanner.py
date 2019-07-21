import subprocess
import re
import threading


def get_name(ip):
    p = subprocess.Popen(["ping", "-a", "-v","5", ip ,"-n", "3", "||", "echo", "%ERRORLEVEL%"], stdout=subprocess.PIPE, shell=True)
    string = (p.communicate()[0]).decode('utf-8')
    x = re.search("Pinging", string)
    count = 0

    # To search %ERRORLEVEL%
    for i in range(len(string)):

        if string[i] == " ":
            count += 1
            if count ==  2:
                name = (string[9:i])
                print("Found a device : " + name)

                # Writing the found device name in a file

                with open("output.txt", 'a') as f:
                    f.write("\n" + name + " : " + ip )

# To get a hit
def ping(ip):
    p = subprocess.Popen(["ping", "-a", "-v","5", ip ,"-n", "3", "||", "echo", "%ERRORLEVEL%"], stdout=subprocess.PIPE, shell=True)


    output = (p.stdout.readlines()[-1]).decode('utf-8')

    #If nothing found on particular ip 

    if str(0) in output[-3]:
        print("No devide found in : " + ip)
        pass

    # If found a device, the thread will be started
    else:
        print("Scanning : " + ip)
        t2 = threading.Thread(target=get_name, args=[ip])  
        t2.start()


for i in range(1, 255):
    ip = "192.168.43.%d"%i
    t1 = threading.Thread(target=ping, args=[ip])
    t1.start()

# ping()

