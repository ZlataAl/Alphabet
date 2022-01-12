def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def I(buf):
    buf[0] = buf[0]+"___     "
    buf[1] = buf[1]+" |      "
    buf[2] = buf[2]+"_|_     "
s = ["","","","","","","",""]
I(s)
I(s)
print(*s, sep="\n")