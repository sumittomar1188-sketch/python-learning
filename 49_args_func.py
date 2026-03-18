# args is just a vaRIABLE LIke we can use anything in the place of aargs like sumit but front is it * complusary
# working - jab user bhot sare parameter de ya fir hame pata na ho ki user kitne parameter dega tab iskause kara jata he 
# ye usko in the form of tuple store kar leta he data ko 


def multiply(*sumit):
    a = 1

    for i in sumit:
        a = a*i
     
    print(sumit)
    return a
x = multiply(1,20,30)

print(x)

# kisi bhi function ka documentation ese dekhenge 
print(print.__doc__)
print(multiply.__doc__) # none aara he kyuki koi documentation diya hi nahi mene


# =========== imp notice ========== 
# order of aarguments matters - normal -> *args then - > **kwargs
# jab ek function meteeno chije use ho to ye order follow karega 
# imp point - "args or "kwargs inko kisi me name deke likh sakte he bss iska dhyan dena hota he *  ** 
