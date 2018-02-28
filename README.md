# Telegram-Passcode-Bruteforce

## Introduction

The Telegram (android) application can be protected with a passcode. This passcode is a 4 digit code. 

This script allows one to bruteforce this passcode.


## Operating mode

The passcode is saved in a hashed form in a XML-file (see below). The hash method is sha256. 
The hash is double salted: the same salt is placed before AND after the passcode. The passcode part is the string UTF-8 representation of the 4 digits. 


## Configuration file

The file "shared_prefs/userconfig.xml" contains something like this :

      <map>
        [...]
        <string name="passcodeHash1">*** SHA256 HASH***</string>
        [...]
        <string name="passcodeSalt">*** BASE64 SALT ***</string>
        [...]
      </map>
      
You must take the "passcodeSalt" and "passcodeHash1" values to run this script.


## Usage

<code>TelegramPasscodeBruteforce.py --salt *the base64 salt* --hash *the hash*</code>
