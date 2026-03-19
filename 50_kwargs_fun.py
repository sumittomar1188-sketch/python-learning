# **  - isko apan function me jab use karenge jab dictionary ke form me likha ho arrgument 


def country (**kwargs):
    for (key,value) in kwargs.items():
        print(key ,"->", value)

country(india= "delhi",shrilanka = "colombo")



# =========== imp notice ========== 
# order of aarguments matters - normal -> *args then - > **kwargs
# jab ek function meteeno chije use ho to ye order follow karega 
# imp point - "args or "kwargs inko kisi me name deke likh sakte he bss iska dhyan dena hota he *  ** 
