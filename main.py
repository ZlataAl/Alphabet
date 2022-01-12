def a(buf):            
    buf[0] = buf[0]+" /\     "
    buf[1] = buf[1]+"/--\    "
    buf[2] = buf[2]+"        "   
def M(buf):
    buf[0] = buf[0]+" |\/|   "
    buf[1] = buf[1]+" |  |   "
    buf[2] = buf[2]+"        "
def S(buf):
    buf[0] = buf[0]+" _      "
    buf[1] = buf[1]+"(_      "
    buf[2] = buf[2]+"__)     " 
def K(buf):
    buf[0] = buf[0]+" |/     "
    buf[1] = buf[1]+" |\     "
    buf[2] = buf[2]+"        "
def H(buf):
    buf[0] = buf[0]+"|_|     "
    buf[1] = buf[1]+"| |     "
    buf[2] = buf[2]+"        "
def N(buf):
    buf[0] = buf[0]+" |\ |   "
    buf[1] = buf[1]+" | \|   "
    buf[2] = buf[2]+"        "
def T(buf):
    buf[0] = buf[0]+" ___    "
    buf[1] = buf[1]+"  |     "
    buf[2] = buf[2]+"  |     "
def C(buf):
    buf[0]=buf[0]+" _      "
    buf[1]=buf[1]+"|       "
    buf[2]=buf[2]+"|_      "
def B(buf):
    buf[0] = buf[0]+" |)     "
    buf[1] = buf[1]+" |_)    "
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
a(s)
M(s)
S(s)
K(s)
H(s)
N(s)
T(s)
C(s)
B(s)
D(s)
W(s)
print(*s, sep="\n")