def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "

def H(buf):
    buf[0] = buf[0]+"|_|     "
    buf[1] = buf[1]+"| |     "
    buf[2] = buf[2]+"        "

s = ["","","","","","","",""]
H(s)
H(s)
print(*s, sep="\n")