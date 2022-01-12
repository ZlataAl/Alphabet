def p(buf):
    buf[0] = buf[0]+"|)      "
    buf[1] = buf[1]+"|       "
    buf[2] = buf[2]+"        "
s = ["","","","","","","",""]
p(s)
p(s)
print(*s, sep="\n")