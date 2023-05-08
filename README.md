# New Challenge Walkthrough



## Pre-requisites:

1. You have `cmgr`.



## Overview

This challenge uses the principles of steganography, searching for hidden files and hashing


## Walkthrough

1. Open the web page
2. Download the image
3. Using nikto look for any hidden files
4. In the results, there are 2 php files
5. Use wget to download both files and examine them
6. One file contains a hashed password while another contains a list of words
7. Use a kali linux tool to get the password from the md5 hash
8. Use the obtained password to extract the flag from the image