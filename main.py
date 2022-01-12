def a(buf):
    buf[0] = buf[0]+"|     "
    buf[1] = buf[1]+"|_    "
    buf[2] = buf[2]+"        "
s = ["","","","","","","",""]
a(s)
a(s)
print(*s, sep="\n")