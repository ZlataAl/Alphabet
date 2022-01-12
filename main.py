def a(buf):            
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def M(buf):
    buf[0] = buf[0]+" |\/|   "
    buf[1] = buf[1]+" |  |   "
    buf[2] = buf[2]+"        "
    
s = ["","","","","","","",""]
M(s)
M(s)
print(*s, sep="\n")