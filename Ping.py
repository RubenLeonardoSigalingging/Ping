#!/usr/bin/env python3


def Ping(kode_oleh="Ruben Leonardo Sigalingging."):
	import subprocess
	from subprocess import call
	import os
	from os import system
	system("clear")


	alamat_target=input("[!] Alamat Target: ")
	hasil_ping=os.popen("ping "+str(alamat_target))
	for ping_ke_alamat_target in hasil_ping:
		print(f"[!] -> {ping_ke_alamat_target}")
Ping()