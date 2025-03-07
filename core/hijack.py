import time  
import random  

def hijack_sms(number):  
    print(f"[*] Targeting {number}...")  
    time.sleep(2)  
    print(f"[+] SMS Intercepted! OTP: {random.randint(1000, 9999)}")  

if __name__ == "__main__":  
    import sys  
    hijack_sms(sys.argv[1])  
