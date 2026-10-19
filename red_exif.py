#!/bin/bash

TARGET_PATH=""

# স্ক্রিন ক্লিয়ার এবং ব্যানার
clear
echo -e "\e[31m"
echo "  ██████╗ ███████╗██████╗     ███████╗██╗  ██╗██╗████████╗"
echo "  ██╔══██╗██╔════╝██╔══██╗    ██╔════╝╚██╗██╔╝██║╚══██╔══╝"
echo "  ██████╔╝█████╗  ██║  ██║    █████╗   ╚███╔╝ ██║   ██║   "
echo "  ██╔══██╗██╔══╝  ██║  ██║    ██╔══╝   ██╔██╗ ██║   ██║   "
echo "  ██║  ██║███████╗██████╔╝    ███████╗██╔╝ ██╗██║   ██║   "
echo "  ╚═╝  ╚═╝╚══════╝╚═════╝     ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   "
echo -e "\e[0m"
echo -e "\e[35m         DEVELOPER BY SABBIR 0X \e[0m"
echo "========================================================="

# মেইন লুপ
while true; do
    
    # ১ নাম্বার অপশনে কারেন্ট পাথ দেখাবে
    if [ -z "$TARGET_PATH" ]; then
        echo -e "\e[33m[1] TARGET PATH (Current: Not Set)\e[0m"
    else
        echo -e "\e[33m[1] TARGET PATH (Current: $TARGET_PATH)\e[0m"
    fi
    
    echo -e "\e[36m[2] ATTACK (Extract Full Information)\e[0m"
    echo -e "\e[32m[3] SEARCH IMAGE (Get Full Path)\e[0m"
    echo -e "\e[31m[4] EXIT\e[0m"
    echo "========================================================="
    
    read -p "Select an option: " choice
    
    case $choice in
        1)
            echo ""
            read -p "Enter Target Path manually: " manual_path
            if [ -f "$manual_path" ]; then
                TARGET_PATH="$manual_path"
                echo -e "\e[32m[+] Target path set successfully: $TARGET_PATH\e[0m"
            else
                echo -e "\e[31m[-] File not found! Please check the path.\e[0m"
            fi
            echo ""
            read -p "Press Enter to return..."
            ;;
            
        2)
            echo ""
            if [ -z "$TARGET_PATH" ]; then
                echo -e "\e[31m[-] No target path set! Please set it using Option 1 or 3 first.\e[0m"
            else
                echo -e "\e[33m[*] Analyzing Image: $TARGET_PATH\e[0m"
                exiftool "$TARGET_PATH"
            fi
            echo ""
            read -p "Press Enter to return..."
            ;;
            
        3)
            echo ""
            read -p "Enter image name (e.g., img_1771 or 1.thailand.jpg): " img_name
            
            # যদি ইউজার এক্সটেনশন (.jpg) না দেয়, তবে আমরা অটোমেটিক এক্সটেনশন চেক করব
            base_name="${img_name%.*}"
            extensions=(".jpg" ".jpeg" ".png" ".webp" ".heic" ".bmp")
            
            search_paths=("/sdcard/Download" "/sdcard/DCIM/Camera" "/sdcard/Pictures" "/sdcard/" "/storage/emulated/0/Download")
            found_path=""
            
            echo -e "\e[33m[*] Searching for image '$img_name'...\e[0m"
            
            # প্রথমে চেক করবে ইউজার এক্সটেনশন সহ দিয়েছে কিনা
            for path in "${search_paths[@]}"; do
                if [ -f "$path/$img_name" ]; then
                    found_path="$path/$img_name"
                    break
                fi
            done
            
            # যদি এক্সটেনশন সহ না পাওয়া যায়, তবে সব কমন এক্সটেনশন দিয়ে খুঁজবে
            if [ -z "$found_path" ]; then
                for path in "${search_paths[@]}"; do
                    for ext in "${extensions[@]}"; do
                        if [ -f "$path/$base_name$ext" ]; then
                            found_path="$path/$base_name$ext"
                            break 2
                        fi
                    done
                done
            fi
            
            if [ -n "$found_path" ]; then
                # ছবি পাওয়া গেলে অটোমেটিক ১ নাম্বারে সেট হবে
                TARGET_PATH="$found_path"
                echo -e "\e[32m[+] Image Found! Full Path: \e[0m"
                echo "    $TARGET_PATH"
                echo -e "\e[36m    [✓] Auto-set to Option 1. Press Enter, then select Option 2 to Attack.\e[0m"
            else
                echo -e "\e[31m[-] Image not found! Check the name or ensure it is in Download/Camera folder.\e[0m"
            fi
            echo ""
            read -p "Press Enter to return..."
            ;;
            
        4)
            echo ""
            echo -e "\e[31mExiting... Goodbye!\e[0m"
            exit 0
            ;;
            
        *)
            echo -e "\e[31mInvalid option! Please select 1, 2, 3, or 4.\e[0m"
            echo ""
            read -p "Press Enter to continue..."
            ;;
    esac
    clear
    # মেনু রিফ্রেশ
    echo -e "\e[31m"
    echo "  ██████╗ ███████╗██████╗     ███████╗██╗  ██╗██╗████████╗"
    echo "  ██╔══██╗██╔════╝██╔══██╗    ██╔════╝╚██╗██╔╝██║╚══██╔══╝"
    echo "  ██████╔╝█████╗  ██║  ██║    █████╗   ╚███╔╝ ██║   ██║   "
    echo "  ██╔══██╗██╔══╝  ██║  ██║    ██╔══╝   ██╔██╗ ██║   ██║   "
    echo "  ██║  ██║███████╗██████╔╝    ███████╗██╔╝ ██╗██║   ██║   "
    echo "  ╚═╝  ╚═╝╚══════╝╚═════╝     ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   "
    echo -e "\e[0m"
    echo -e "\e[35m         DEVELOPER BY SABBIR 0X \e[0m"
    echo "========================================================="
done
