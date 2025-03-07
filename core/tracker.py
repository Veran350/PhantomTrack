import phonenumbers  
import requests  
import sqlite3  

def validate_naija_number(number):  
    try:  
        parsed = phonenumbers.parse(number, "NG")  
        return phonenumbers.is_valid_number(parsed)  
    except:  
        return False  

def get_carrier(number):  
    conn = sqlite3.connect('core/carriers.db')  
    c = conn.cursor()  
    prefix = number[3:6]  
    c.execute("SELECT carrier FROM carriers WHERE prefix=?", (prefix,))  
    return c.fetchone()[0]  

def track(number):  
    if not validate_naija_number(number):  
        print("Invalid Nigerian number! Use +2348012345678")  
        return  

    # Get IP-based location  
    ip = requests.get("https://api.ipify.org").text  
    loc = requests.get(f"http://ip-api.com/json/{ip}").json()  

    print(f"""  
[+] Tracking: {number}  
Carrier: {get_carrier(number)}  
City: {loc.get('city', 'Lagos (Default)')}  
Coordinates: {loc.get('lat', '6.5244')}, {loc.get('lon', '3.3792')}  
""")  

if __name__ == "__main__":  
    import sys  
    track(sys.argv[1])  
