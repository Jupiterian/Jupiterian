# Overview
This is a hash checking script. To use, simply paste the original hash, the file path, and the algorithm you want it to compute in. Then it will tell you if the checksums match.

# COMMON ERRORS
The following are common errors that people face.


## FIPS CRYPTOGRAPHY IS ENABLED
If you have enabled on FIPS Cryptography algorithms to run on your computer, then you will not be able to use old checksums such as MD5 and SHA1. 
Fix:
Open secpol.msc
Go to Local Policies > Security Options
Scroll down and double click System Cryptography: Use FIPS Compliant algorithms for encryption, hashing, and signing
Set the value to "Disabled"

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
