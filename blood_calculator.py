#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:28:10 2022

@author: jisellehavas
"""

def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice:")
        if choice == "9":
            return
    
interface()