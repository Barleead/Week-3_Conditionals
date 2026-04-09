# Author: Barbara Adkins

from datetime import datetime

analyst_name = input("What is the analyst's name? ")
username = input("What is the username being analyzed? ")
login_attempts = int(input("Enter the number of login attempts: "))
privileged_user = input("Is this a privileged user? (yes/no): ")

print("======================================")
print(" Cyber Defense - Login Attempt Report ")
print("======================================")

print(f"Analyst: {analyst_name}")
print(f"User: {username}")
print(f"Failed Attempts: {login_attempts}")

if (login_attempts > 5) and (privileged_user.lower() == "yes"):
    print("Risk Level: High")
    print("[!] ALERT: Privileged acount shows multiple failed logins")
elif login_attempts > 5:
    print("Risk Level: Moderate")
    print("[!] WARNING: User has several failed login attempts.")
elif login_attempts > 0 and login_attempts <= 5:
    print("Risk Level: Low Risk")
    print("[-] Some failed attempts observed.")
else:
    print("Risk Level: Informational")
    print("[+] No failed logins recorded. ")

print("Report Generated: ", datetime.now())
