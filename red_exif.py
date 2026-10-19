import os
import sys
import time
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama pillow")
    from colorama import Fore, Style, init
    init(autoreset=True)

target_path = "Not Set"
search_folders = [
    "/sdcard/DCIM/Camera/",
    "/sdcard/Download/",
    "/sdcard/Pictures/",
    "/storage/emulated/0/DCIM/Camera/",
    "/storage/emulated/0/Download/",
    "/storage/emulated/0/Pictures/"
]

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    clear_screen()
    print(Fore.RED + "==================================================")
    print(Fore.RED + Style.BRIGHT + "  ____  _____ ____     _____  __  __ ___ _____ ")
    print(Fore.RED + Style.BRIGHT + " |  _ \| ____|  _ \   | ____| \ \/ /|_ _|_   _|")
    print(Fore.RED + Style.BRIGHT + " | |_) |  _| | | | |  |  _|    \  /  | |  | |  ")
    print(Fore.RED + Style.BRIGHT + " |  _ <| |___| |_| |  | |___   /  \  | |  | |  ")
    print(Fore.RED + Style.BRIGHT + " |_| \_\_____|____/   |_____| /_/\_\|___| |_|  ")
    print(Fore.RED + "==================================================")
    print(Fore.MAGENTA + Style.BRIGHT + "            DEVELOPER BY SABBIR ØX")
    print(Fore.RED + "==================================================")
    print("")

def show_menu():
    print(Fore.CYAN + f"[1] " + Fore.WHITE + f"TARGET PATH (Current: {target_path})")
    print(Fore.CYAN + f"[2] " + Fore.WHITE + f"ATTACK (Extract Full Information)")
    print(Fore.CYAN + f"[3] " + Fore.WHITE + f"SEARCH IMAGE (Get Full Path)")
    print(Fore.RED + f"[4] " + Fore.WHITE + f"EXIT")
    print(Fore.RED + "==================================================")

def find_image_path(image_name):
    for folder in search_folders:
        full_path = os.path.join(folder, image_name)
        if os.path.exists(full_path):
            return full_path
    return None

def get_gps_coordinates(exif_data):
    gps_info = {}
    if TAGS.get(34853) in exif_data:
        gps_data = exif_data[34853]
        for key, value in gps_data.items():
            decode = GPSTAGS.get(key, key)
            gps_info[decode] = value
    return gps_info

def convert_to_degrees(value):
    d, m, s = value
    return d + (m / 60.0) + (s / 3600.0)

def attack_image(image_path):
    print(Fore.YELLOW + f"\n[*] Analyzing Image: {image_path}\n")
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        if not exif_data:
            print(Fore.RED + "[-] No EXIF data found in this image.")
            return
            
        print(Fore.CYAN + "--- FULL IMAGE METADATA ---")
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "GPSInfo":
                continue
            if isinstance(value, bytes):
                continue
            print(Fore.WHITE + f"[*] {tag}: {value}")
            
        gps_info = get_gps_coordinates(exif_data)
        if gps_info:
            print(Fore.CYAN + "\n--- GPS LOCATION FOUND ---")
            lat = None
            lon = None
            if "GPSLatitude" in gps_info and "GPSLatitudeRef" in gps_info:
                lat = convert_to_degrees(gps_info["GPSLatitude"])
                if gps_info["GPSLatitudeRef"] != "N":
                    lat = 0 - lat
            if "GPSLongitude" in gps_info and "GPSLongitudeRef" in gps_info:
                lon = convert_to_degrees(gps_info["GPSLongitude"])
                if gps_info["GPSLongitudeRef"] != "E":
                    lon = 0 - lon
                    
            if lat and lon:
                print(Fore.GREEN + Style.BRIGHT + f"[+] Latitude : {lat}")
                print(Fore.GREEN + Style.BRIGHT + f"[+] Longitude: {lon}")
                print(Fore.YELLOW + f"[*] Map Link : https://www.google.com/maps/place/{lat},{lon}")
        else:
            print(Fore.RED + "\n[-] No GPS data found in this image.")
            
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")

def main():
    global target_path
    while True:
        show_banner()
        show_menu()
        
        choice = input(Fore.YELLOW + "\nSelect an option: " + Fore.WHITE)
        
        if choice == '1':
            target_path = input(Fore.CYAN + "Enter Full Path of Image: ").strip()
            if not target_path:
                target_path = "Not Set"
                
        elif choice == '2':
            if target_path == "Not Set":
                print(Fore.RED + "\n[!] Please set Target Path first (Option 1).")
                time.sleep(2)
                continue
            attack_image(target_path)
            input(Fore.YELLOW + "\nPress Enter to return...")
            
        elif choice == '3':
            search_name = input(Fore.CYAN + "\nEnter Image Name (e.g., 1.thailand): ").strip()
            if not search_name:
                continue
            if not search_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                search_name += ".jpg"
                
            print(Fore.YELLOW + f"\n[*] Searching for '{search_name}'...")
            time.sleep(1)
            found_path = find_image_path(search_name)
            if found_path:
                print(Fore.GREEN + Style.BRIGHT + f"[✓] IMAGE FOUND! Full Path:")
                print(Fore.CYAN + f"{found_path}")
                print(Fore.YELLOW + "[*] Copy this path and paste it in Option 1.")
            else:
                print(Fore.RED + f"[-] Image '{search_name}' not found in standard folders.")
            input(Fore.YELLOW + "\nPress Enter to return...")
            
        elif choice == '4':
            print(Fore.RED + "Exiting... Goodbye!")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option!")
            time.sleep(1)

if __name__ == "__main__":
    main()
