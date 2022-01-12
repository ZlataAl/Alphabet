def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def D(buf):
    buf[0] = buf[0]+"|\      "
    buf[1] = buf[1]+"| |     "
    buf[2] = buf[2]+"|/      "

s = ["","","","","","","",""]
D(s)
D(s)
print(*s, sep="\n")