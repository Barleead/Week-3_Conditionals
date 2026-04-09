# failed_logins = 10

# if failed_logins > 3:
#     print("[!] Warning: Multiple failed login attempts detected!")
# else:
#     print("[+] Normal login behavior.")

# ## Part Two ##

# username = input("Enter Username: ")

# failed_logins = int(input("Enter the number of failed login attempts: "))

# if failed_logins > 5:
#     print(f"[!] ALERT: {username} has {failed_logins} failed logins!")
# else:
#     print(f"User {username} appears normal.")

# ## Part Three ##

# usernamesername = input("Enter Username: ")
# critical_user = input("Is this a privileged user? (yes/no): ")

# failed_logins = int(input("Enter the number of failed login attempts: "))

# if failed_logins > 5 and critical_user.lower() == "yes":
#     print("[*] CRITICAL ALERT: Privileged acount under attack!")
# elif failed_logins > 5:
#     print("[!] ALERT: Multiple failed logims detected.")
# elif failed_logins > 0:
#     print("[-] NOTice: Some failed attempts observed.")
# else:
#     print("[+] No failed logins recorded. ")

## Part 4##
username = input("Enter Username: ")
critical_user = input("Is this a privileged user? (yes/no): ")

failed_logins = int(input("Enter the number of failed login attempts: "))

if failed_logins > 5 and critical_user.lower() == "yes":
    print("[*] CRITICAL ALERT: Privileged acount under attack!")
elif failed_logins > 5:
    print("[!] ALERT: Multiple failed logims detected.")
elif failed_logins > 0:
    print("[-] NOTice: Some failed attempts observed.")
else:
    print("[+] No failed logins recorded. ")

print("\n=== Login Attempt Summary ===")
print(f"Username: {username}")
print(f"Failed Attempts: {failed_logins}")
print(f"Privileged Account: {critical_user}")
