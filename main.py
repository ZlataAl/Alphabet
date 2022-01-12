def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def Q(buf):
    buf[0]=buf[0]+" __      "
    buf[1]=buf[1]+"|  |     "
    buf[2]=buf[2]+" --\     "  
s = ["","","","","","","",""]
Q(s)
Q(s)
print(*s, sep="\n")