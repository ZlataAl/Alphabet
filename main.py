def a(buf):
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "
def D(buf):
    buf[0] = buf[0]+"|\      "
    buf[1] = buf[1]+"| |     "
    buf[2] = buf[2]+"|/      "
def W(buf):
    buf[0] = buf[0]+" \    / "
    buf[1] = buf[1]+"  \/\/  "
    buf[2] = buf[2]+"        "

s = ["","","","","","","",""]
a()
D()
W(s)
print(*s, sep="\n")