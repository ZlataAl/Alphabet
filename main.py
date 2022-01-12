def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def G(buf):
    buf[0]=buf[0]+" __       "
    buf[1]=buf[1]+"|  _      "
    buf[2]=buf[2]+"|__|      "  

s = ["","","","","","","",""]
G(s)
G(s)
print(*s, sep="\n")