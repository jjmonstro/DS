import os
os.system("cls")
v=[41,72,39,4,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

a=0

for i in range(10):
    if v[i]<v[i+1] and v[i]<v[i+2] and v[i]<v[i+3] and v[i]<v[i+4] and v[i]<v[i+5]:
        v[i+a]=v[i]     
        a=a+1

for i in range(10):
    print(v[i])

# FUCK!!