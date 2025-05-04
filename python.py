import os
import webbrowser
import uuid

# Open Telegram channel on first run
webbrowser.open("https://t.me/+PFbp1Ayc_1I3ZTFk")

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# ASCII Banner
banner = r'''
██████╗  █████╗ ██████╗ ██╗  ██╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║  ██║██╔════╝██╔══██╗
██████╔╝███████║██████╔╝█████╔╝ ███████║█████╗  ██████╔╝
██╔═══╝ ██╔══██║██╔═══╝ ██╔═██╗ ██╔══██║██╔══╝  ██╔══██╗
██║     ██║  ██║██║     ██║  ██╗██║  ██║███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            Created by 𝑫𝑨𝑹𝑲 𝑯𝑨𝑪𝑲𝑬𝑹
'''

print(banner)
print("\nWelcome to the Fake Link Generator!\n")
print("Choose a target application:\n")
apps = [
    "Facebook", "PUBG Mobile", "Free Fire", "PES Mobile", "FIFA Mobile",
    "Instagram", "Snapchat", "TikTok", "Twitter", "Roblox",
    "Netflix", "Spotify", "PUBG Lite", "Call of Duty", "Fortnite"
]

for i, app in enumerate(apps, 1):
    print(f"{i}. {app}")

choice = input("\nEnter the number of the app: ")

try:
    index = int(choice) - 1
    if 0 <= index < len(apps):
        selected_app = apps[index].lower().replace(" ", "")
        user_id = str(uuid.uuid4())[:8]
        fake_link = f"https://yourtool.site/{selected_app}/login?id={user_id}"
        print(f"\n[+] Your fake link for {apps[index]}:\n{fake_link}\n")
    else:
        print("[!] Invalid choice.")
except ValueError:
    print("[!] Please enter a valid number.")
