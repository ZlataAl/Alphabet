def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def S(buf):
    buf[0] = buf[0]+" _      "
    buf[1] = buf[1]+"(_      "
    buf[2] = buf[2]+"__)     " 
s = ["","","","","","","",""]
S(s)
S(s)
print(*s, sep="\n")