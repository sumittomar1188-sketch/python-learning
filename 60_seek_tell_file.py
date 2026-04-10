#================== tell ==============
#tell - tell function tells us ki curser memory me kha par he means next konsa char print hoga 
with open("sample1.txt","r") as f :
    print(f.read(10))
    print(f.tell()) # yha ye bata dega ki next kosne word print hone wala he 


# =============== seek ============
# seek - ye hame allow karta he ki hame konsi jgh jana ho ja sakte he words me lets take an example 
with open("sample1.txt","r") as f1 :
    print(f1.read(10))
    print(f1.read(10))
    f1.seek(0) # issse curser 0 pe vapis chl jaega or fir vapis se print hoga
    print(f1.read())

# seek during write 
with open("seek.txt","w") as f2 :
    f2.write("hello")
    f2.seek(0) # ye curser ko 0 par la dega
    f2.write("X") # or change kar dega 
    f2.seek(3)
    f2.write("c")

