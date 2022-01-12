def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "

def B(buf):
    buf[0] = buf[0]+" |)     "
    buf[1] = buf[1]+" |_)    "
    buf[2] = buf[2]+"        "
    
s = ["","","","","","","",""]
B(s)
B(s)
print(*s, sep="\n")
