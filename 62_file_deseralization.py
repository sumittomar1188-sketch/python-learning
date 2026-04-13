import json
with open ("jason.demo","r") as f :
    a = json.load(f)
    print(a)
    print(type(a))

# agar file me tuple he to ye usko list ke form me return ya decirialized karega
with open ("demo.txt","r") as f1 :
    a = json.load(f1)
    print(a)