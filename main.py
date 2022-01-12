def R(buf):
    buf[0] = buf[0]+"|)      "
    buf[1] = buf[1]+"|\      "
    buf[2] = buf[2]+"        "
s = ["","","","","","","",""]
R(s)
R(s)
print(*s, sep="\n")