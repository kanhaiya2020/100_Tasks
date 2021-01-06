from datetime import datetime

# current date and time
# now = datetime.now()

# timestamp = datetime.timestamp(now)
# print(str(int(timestamp)))
# print("timestamp =", timestamp)

import os

# 128 bit, 192 bit and 256 bit keys
key_128 = os.urandom(16)
key_192 = os.urandom(24)
key_256 = os.urandom(32)
print(key_256)
key = "This_key_for_demo_purposes_only!"
print(len(key))
# Note:-> It's used for convert the date and time to any timezone as your choice or it's universal time and date  