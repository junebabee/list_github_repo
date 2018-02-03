#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:36:46 2018

@author: June
"""

#This program will call the github API and return the names of public repositories that are accessible to my github account.

import requests

def try_again():
    try_again = raw_input('Do you want to try again? (Y/N):')
    if try_again.upper()[0] == 'Y': 
        Get_User = raw_input('Please enter a github user name:')  
        Get_Repo(Get_User)
    else:
        return
    
Get_User = raw_input('Please enter a github user name:')

def Get_Repo(Get_User):
    url = 'https://api.github.com/users/'+ Get_User +'/repos'
    repo = requests.get(url).json()
    response = requests.get(url)
    if response.status_code == 200:
        for i in range(0,len(repo)):
            print repo[i]['name']
            i += 1
    elif response.status_code == 404:
        print 'No user exist!'
        try_again()
    else:
        print 'Oops! something is wrong!'
        try_again()
        
Get_Repo(Get_User)
