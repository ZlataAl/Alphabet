def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
def F(buf):
    buf[0] = buf[0]+"  _     "
    buf[1] = buf[1]+" |_     "
    buf[2] = buf[2]+" |      "
s = ["","","","","","","",""]
F(s)
F(s)
print(*s, sep="\n")