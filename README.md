# pwHasher
Easily hash text (like passwords)

Why do I need / want this?
--------------------------
I use some systems where I need to provide a hashed password for use later in authentication (like HAProxy ACLs).  This utility will list the available hash algorithms available on your computer and then hash your input text with that algorithm.

Usage
------
1. Make the script executable: ```chmod a+x pwHasher.py```
2. Run the script.
3. Choose a hash method from the list.
4. Enter the text to be hashed.
