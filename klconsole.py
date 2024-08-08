#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyfiglet import Figlet
from colorama import Fore, init, Style
import threading
import requests
import time
import sys
import random
import os
import base64
import argparse
import platform
import getpass
import subprocess
import socket
from netaddr import IPNetwork, IPAddress
from queue import Queue

init()

def banner():
    """Prints a random banner from a set of predefined banners."""
    banners = [
        """
            ::      ::
            ::     ::
            ::    ::
            ::  ::
            ::::
            :: ::
            ::  ::
            ::   ::
            ::    ::      ::
            ::     ::     ::
                   killer cyber
                          ::
                          ::
                          ::
                          ::
                          ::
                          ::::::::
        """,
        """
        +------------------------------------------------+
        | [+] Team: Killer Cyber Team     |
        | [+] Modules: 47                          |
        | [+] exploits: 14                           |
        | [+] payloads: 2                           |
        +------------------------------------------------+
        """,
        """    
        _     _     __    ___   _      __   ___   _     ____ 
        | |_/ | |   / /`  / / \ | |\ | ( (` / / \ | |   | |_  
        |_| \ |_|__ \_\_, \_\_/ |_| \| _)_) \_\_/ |_|__ |_|__ 
        """
    ]
    print(random.choice(banners))

def menu():
    """Displays the main menu."""
    print("" + Fore.RESET)
    print(f"""
=[ {Fore.YELLOW}Killer-Framework console v1.0.01-dev-bbf096e{Style.RESET_ALL}    ]
+ -- --=[ 14 exploits - 47 auxiliary - 5 post      ]
+ -- --=[ 14 payloads - 5 encoders - 0 nops        ]
+ -- --=[ 40 evasion -                             ]
+ -- --=[ İntikam21 Framework - 2 shodan - 90 network]
İntikam21 Documentation: https://sites.google.com/view/intilam21-cyber-team/kay%C4%B1t
""" + Fore.RESET)

def get_prompt(module=None, exploit=None, payload=None, sn=None, s=None):
    """Generates the prompt string based on the provided parameters."""
    return (f"klconsole ({module}) >" if module else
            f"klconsole exploit({exploit}) >" if exploit else
            f"klconsole payload({payload}) >" if payload else
            f"klconsole {sn}({s}) >" if sn and s else
            "klconsole >")

prompt = get_prompt()
banner()
menu()
while True:
	klr = input(prompt)
	if klr == "?" or klr.lower() == "help":
		print("""
 	Commands     Function
    --------------------   -----------------
     set                    setting settings
     ?                        help menu
     help                  help menu
     banner             show banners
     show                commands infos
     connect           connecting ip's
     trojan                trojan
		""")
	if klr.startswith("set"):	
		f = klr[4:]
		st = f[f.find("= ") + 2:]
		zr = f[:f.find("=")]
		format_part = f[f.find("> ") + 2:] if "> " in f else None
		print(f"{zr} ==> {st} > {format_part}")
	if klr.startswith("banner") or klr == "banner":
		banner()
		menu()