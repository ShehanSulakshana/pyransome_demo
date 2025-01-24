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

passphrase= input("\n[#] Enter the pass phrase to continue : ").strip()

if passphrase == "pyransome_demo*shehanss":

	with open("thekey.key","rb") as keyfile:
		key = keyfile.read()
		cipher_suite = Fernet(key)

	for file in files:
		with open(file,"rb") as con_file:
			content = con_file.read()

		with open(file,"wb") as dec_file:
			dec_content = cipher_suite.decrypt(content)
			dec_file.write(dec_content)

	print ("[+++] OK BUDDY ALL YOU FILES WERE DECRYPTED SUCCESFULLY... ")

else :
	print ("[-] WRONG PASS PHRASE , BYE BYE...")
