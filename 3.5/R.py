# with open(input(), "rb") as source:
#    bytes = 0
#    while source.read(1):
#        bytes += 1

import os
import math

bytes = os.stat(input()).st_size

gbyte = 1024**3
mbyte = 1024**2
kbyte = 1024**1

if bytes >= gbyte:
    measure = gbyte
    suffix = "ГБ"
elif bytes >= mbyte:
    measure = mbyte
    suffix = "МБ"
elif bytes >= kbyte:
    measure = kbyte
    suffix = "КБ"
else:
    measure = 1
    suffix = "Б"

print(f"{math.ceil(bytes / measure)}{suffix}")
