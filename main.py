def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def N(buf):
    buf[0] = buf[0]+" |\ |   "
    buf[1] = buf[1]+" | \|   "
    buf[2] = buf[2]+"        "
    
s = ["","","","","","","",""]
N(s)
N(s)
print(*s, sep="\n")