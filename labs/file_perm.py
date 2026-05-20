import os
import stat

try:
    os.remove("labuser.pem")
except:
    print ("File does not exist")

print("Download the new file now..")
input ("Press Enter to continue...")

try:
    os.chmod("labuser.pem" , stat.S_IREAD)
except:
    print ("File does not exist")