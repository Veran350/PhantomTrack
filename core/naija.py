import os  
from pyfiglet import Figlet  

# Massive ASCII Heading  
banner = Figlet(font="big")  
print(banner.renderText("NAIJA HIJACK"))  
print("v5.0 | Track & Hijack ANY Nigerian Number\n")  

def menu():  
    print("""  
┌── Main Menu ────────────────────────────────  
│                                              
│  /track <number>   : Live GPS & carrier      
│  /hijack <number>  : Steal OTP/SMS           
│  /exit             : Kill the tool           
│                                              
└──────────────────────────────────────────────""")  

    while True:  
        cmd = input("\nnaija@root~$ ").strip()  
        if cmd.startswith("/track"):  
            os.system(f"python core/tracker.py {cmd.split()[-1]}")  
        elif cmd.startswith("/hijack"):  
            os.system(f"python core/hijack.py {cmd.split()[-1]}")  
        elif cmd == "/exit":  
            break  
        else:  
            print("[!] Invalid command")  

if __name__ == "__main__":  
    menu()  
