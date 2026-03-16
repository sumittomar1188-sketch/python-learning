# example
# pehle ham ek set banaenge uske andar valyues ko dal denge for iteration ke liye 
print({i for i in range (1,11)})
print({i for i in range (1,20) if (i%5==0)})
print({i**2 for i in range(1,30)})


distance = {"mumbai":1000,
            "delhi":500,
            "kolkata":2000,
            "ra,eshvaram":3000}
print(distance for distance in distance)