import os
import time

print("""
*---------------------*
|                     |
| Easy script for you |
|                     |
*---------------------*

print
	""")
fff = input("[???] Do you want install metasploit? (y/n): ")
if fff == "y":
	print("=======================================")
	print("[+] Jesus, it will take a lot of time!!")
	print("=======================================")
	os.system ("pkg update -y")
	os.system ("pkg install -y curl")
	os.system ("cd /data/data/com.termux/files/home && curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh")
	os.system ("cd /data/data/com.termux/files/home && chmod +x metasploit.sh")
	os.system ("cd /data/data/com.termux/files/home && bash metasplot.sh")
	os.system ("cd /data/data/com.termux/files/home && bundle init")
	os.system ("cd /data/data/com.termux/files/home && gem install bundler -v 1.16.1")
	os.system ("cd /data/data/com.termux/files/home && bundle install -j5")
	os.system ("cd /data/data/com.termux/files/home && bash metasplot.sh")
	print("=====================================")
	print("[+] Metasploit installed successfully")
	print("Type 'msfconsole' to start.")
	print("=====================================")


elif fff == "n":
	os.system("cd /data/data/com.termux/files/home")
	os.system("pkg install -y hydra")
	os.system("cd /data/data/com.termux/files/home")
	print("====================================")
	print("[+] hydra installed successfully")
	print("Type 'hydra' to start.")
	print("====================================")