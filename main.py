def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def T(buf):
    buf[0] = buf[0]+" ___    "
    buf[1] = buf[1]+"  |     "
    buf[2] = buf[2]+"  |     "
    
s = ["","","","","","","",""]
T(s)
T(s)
print(*s, sep="\n")