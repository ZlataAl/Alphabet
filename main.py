def z(buf):  
    buf[0] = buf[0]+"__      "
    buf[1] = buf[1]+" /      "
    buf[2] = buf[2]+"/_      "
s = ["","","","","","","",""]
z(s)
z(s)
print(*s, sep="\n")