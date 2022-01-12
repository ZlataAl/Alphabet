def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
    
def J(buf):
    buf[0] = buf[0]+" __     "
    buf[1] = buf[1]+"  |     "
    buf[2] = buf[2]+" _/     "

    
s = ["","","","","","","",""]
J(s)
J(s)
print(*s, sep="\n")