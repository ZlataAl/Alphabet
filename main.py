def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def Y(buf):
    buf[0] = buf[0]+"\ /     "
    buf[1] = buf[1]+" |      "
    buf[2] = buf[2]+" |      "   
s = ["","","","","","","",""]
Y(s)
Y(s)
print(*s, sep="\n")