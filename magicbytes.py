#!/usr/bin/python
import sys
import os

print("___  ___            _     ______       _                           ")                          
print("|  \/  |           (_)    | ___ \     | | github.com/Haxrein       ")                         
print("| .  . | __ _  __ _ _  ___| |_/ /_   _| |_ ___  ___   _ __  _   _  ") 
print("| |\/| |/ _` |/ _` | |/ __| ___ \ | | | __/ _ \/ __| | '_ \| | | | ")
print("| |  | | (_| | (_| | | (__| |_/ / |_| | ||  __/\__ \_| |_) | |_| | ")
print("\_|  |_/\__,_|\__, |_|\___\____/ \__, |\__\___||___(_) .__/ \__, | ")
print("               __/ |              __/ |              | |     __/ | ")
print("              |___/              |___/               |_|    |___/\n")
                                                                  

png = "0x89504E470D0A1A0A0000000D"
png_int = int(png, 16)
png_hex = hex(png_int)

jpg = "0xFFD8FFE000104A4649460001"
jpg_int = int(jpg, 16)
jpg_hex = hex(jpg_int)

if len(sys.argv) != 5:
    print("Example usage: magicbytes.py -i broken.png -m png")
    exit()

inputfile = sys.argv[2]
magic = sys.argv[4]

if magic != "png" and magic != "jpg" and magic != "jpeg": 
    print("Magicbytes.py only supports png, jpeg and jpg!")
    exit()

with open(inputfile, 'rb') as f:
    content = f.read().hex()
    if magic == "png": 
        content = content.replace(content[0:24], png_hex[2:])
    elif magic == "jpeg" or "jpg":
        content = content.replace(content[0:24], jpg_hex[2:])


with open(inputfile, 'wb') as f:
    f.write(bytes.fromhex(content))

extension = "." + magic

base = os.path.splitext(inputfile)[0]
os.rename(inputfile, base + extension)

print("Magic bytes has been changed of", inputfile, "as", magic)
