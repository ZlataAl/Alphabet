def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
def E(buf):
    buf[0] = buf[0]+"  _     "
    buf[1] = buf[1]+" |_     "
    buf[2] = buf[2]+" |_     "

s = ["","","","","","","",""]
E(s)
E(s)
print(*s, sep="\n")