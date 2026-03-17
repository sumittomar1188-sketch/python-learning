# editing kust like adding hota he bss existing value ko change karr dete he same key se lets take an exxample
s = {"name":"sumit",
      "age":18,
      "subject":{"math":80,
                 "english":90,
                 "science":100}}


# jese ki apan ko age or  english ke number ko edit karna he to 

s["age"]=19
print(s)  # isme age ki value change ho gyi he 
s["subject"]["math"]= 90
print(s)