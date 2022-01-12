def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
def C(buf):
    buf[0]=buf[0]+" _      "
    buf[1]=buf[1]+"|       "
    buf[2]=buf[2]+"|_      "
s = ["","","","","","","",""]
C(s)
C(s)
print(*s, sep="\n")