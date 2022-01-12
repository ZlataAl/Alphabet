def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def K(buf):
    buf[0] = buf[0]+" |/     "
    buf[1] = buf[1]+" |\     "
    buf[2] = buf[2]+"        "
    
s = ["","","","","","","",""]
K(s)
K(s)
print(*s, sep="\n")