# Python 3 code to demonstrate the 
# working of MD5 (string - hexadecimal) 

import hashlib 

# initializing string 
str2hash = "GeeksforGeeks1"

# encoding GeeksforGeeks using encode() 
# then sending to md5() 
result = hashlib.md5(str2hash.encode()) 
print(result)
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of hash is : ", end ="") 
# for var in result:
#     print(var)
ss = result.hexdigest()
print(ss) 

# Note: It can not be decrypted or reverse into the plain text


