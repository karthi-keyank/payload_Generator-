# PL-generator-
You used to generate payload,but can't be use this tool without metasploit,so you must install metasploit 

# installation 
```
git clone https://github.com/karthi-keyank/PL-generator-.git
```
```
cd PL-generator
```
```
apt update && apt upgrade -y && apt-get install python3 && pip install -r requirements.txt
```
```
python msfvenom.py
```
# Usage
- the tool used to just create payloads from msfvenom
- not for hacking
- I write only 16 basic payload for your look
- but you can generate any payload
- if you seeing any error,make issue
- if want add any features,make comment
- thanks for Install
# Solutions for comman Errors 
- FileNotFoundError: install metasploit-framework by pkg install metasploit
- command Error: it's your typing Error,if you want to see all payload,type
```
  msfvenom --list all payloads
```
- moduleNotFoundError: Install all necessary modules
```
pip install -r requirements.txt
```
or
```
pip install <modules>
```
- module:colorama,termcolor,subprocess

