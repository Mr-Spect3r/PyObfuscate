# -*- coding:utf8 -*-
# Best Encrypter PYTHON

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'
tr = f'{rd}[{gn}+{rd}]{gn}'
fls = f'{rd}[{lrd}-{rd}]{lrd}'

try:
    import os
    import sys
    import zlib
    import gzip
    import lzma
    import time
    import base64
    import marshal
    import py_compile
except Exception as F:
	print (f"{fls}Module Error {F}\n\nTo install the module, enter the following command: \n{k}pip install {F}")

def clear():
    if 'Windows' in __import__("platform").uname():
        os.system("cls")
    else:
    	os.system("clear")	
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit(f"\n{fls}Your Python Version is not Supported!")

zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
gzi = lambda in_ : gzip.compress(in_)
lzm = lambda in_ : lzma.compress(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))

def banner():
    clear()
    print(f'''   {k}                                      
         .+#-                                           
         .+@@%-                                         
           .*@@%-   {cn}          ..     {k}                   
             .*@@%- {cn}         .@@# {k}                      
               .*@@%- {cn}       +@@-    {k}                   
               :#@@@@%-{cn}      @@#     -@@=               
             :#@@*.{k}.+@@%-{cn}   =@@:      =@@@=             
           :#@@*. {k}   .+@@#:{cn}  -+         =@@@=           
         :#@@*.   {k}     .+@@%-   {cn}          =@@@=         
        +@@@-     {k}       .#@@#:   {cn}          %@@%.       
         :#@@*.          {k} #@@@@%-        {cn} =@@@=         
        {cn}   -#@@*.        -@@+.{k}*@@#:    {cn} =@@@=           
        {cn}     :#@@#:      %@@  {k} .+@@%- {cn} :#%=             
               :#@*  {cn}   -@@=    {k} .*@@%-                 
                     {cn}   %@%     {k}   .+@@%-               
                     {cn}  -@@-        {k}  .*@@%-             
                         .        {k}     .+@@%-           
                                   {k}      .*@@%-         
                                   {k}        .+*:
    {gn}Python Obfuscate | TG: @MrMrEsfelurm                            
                                   ''')

def menu():
    print (f'''{k}
{rd}[{yw}1{rd}] {gn}Encode Marshal
{rd}[{yw}2{rd}] {gn}Encode Zlib
{rd}[{yw}3{rd}] {gn}Encode Base16
{rd}[{yw}4{rd}] {gn}Encode Base32
{rd}[{yw}5{rd}] {gn}Encode Base64
{rd}[{yw}6{rd}] {gn}Encode Lzma
{rd}[{yw}7{rd}] {gn}Encode Gzip
{rd}[{yw}8{rd}] {gn}Encode Zlib,Base16
{rd}[{yw}9{rd}] {gn}Encode Zlib,Base32
{rd}[{yw}10{rd}] {gn}Encode Zlib,Base64
{rd}[{yw}11{rd}] {gn}Encode Gzip,Base16
{rd}[{yw}12{rd}] {gn}Encode Gzip,Base32
{rd}[{yw}13{rd}] {gn}Encode Gzip,Base64
{rd}[{yw}14{rd}] {gn}Encode Lzma,Base16
{rd}[{yw}15{rd}] {gn}Encode Lzma,Base32
{rd}[{yw}16{rd}] {gn}Encode Lzma,Base64
{rd}[{yw}17{rd}] {gn}Encode Marshal,Zlib
{rd}[{yw}18{rd}] {gn}Encode Marshal,Gzip
{rd}[{yw}19{rd}] {gn}Encode Marshal,Lzma
{rd}[{yw}20{rd}] {gn}Encode Marshal,Base16
{rd}[{yw}21{rd}] {gn}Encode Marshal,Base32
{rd}[{yw}22{rd}] {gn}Encode Marshal,Base64
{rd}[{yw}23{rd}] {gn}Encode Marshal,Zlib,B16
{rd}[{yw}24{rd}] {gn}Encode Marshal,Zlib,B32
{rd}[{yw}25{rd}] {gn}Encode Marshal,Zlib,B64
{rd}[{yw}26{rd}] {gn}Encode Marshal,Lzma,B16
{rd}[{yw}27{rd}] {gn}Encode Marshal,Lzma,B32
{rd}[{yw}28{rd}] {gn}Encode Marshal,Lzma,B64
{rd}[{yw}29{rd}] {gn}Encode Marshal,Gzip,B16
{rd}[{yw}30{rd}] {gn}Encode Marshal,Gzip,B32
{rd}[{yw}31{rd}] {gn}Encode Marshal,Gzip,B64
{rd}[{yw}32{rd}] {gn}Encode Marshal,Zlib,Lzma,B16
{rd}[{yw}33{rd}] {gn}Encode Marshal,Zlib,Lzma,B32
{rd}[{yw}34{rd}] {gn}Encode Marshal,Zlib,Lzma,B64
{rd}[{yw}35{rd}] {gn}Encode Marshal,Zlib,Gzip,B16
{rd}[{yw}36{rd}] {gn}Encode Marshal,Zlib,Gzip,B32
{rd}[{yw}37{rd}] {gn}Encode Marshal,Zlib,Gzip,B64
{rd}[{yw}38{rd}] {gn}Encode Marshal,Zlib,Lzma,Gzip,B16
{rd}[{yw}39{rd}] {gn}Encode Marshal,Zlib,Lzma,Gzip,B32
{rd}[{yw}40{rd}] {gn}Encode Marshal,Zlib,Lzma,Gzip,B64
{rd}[{yw}41{rd}] {gn}Simple Encode
{rd}[{yw}42{rd}] {gn}Exit

    ''')
    print ('')
class FileSize:
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(f"{tr} Encoded File Size : %s\n" % self.datas(dts))
# FileSize('rec.py')

# Encode Menu
def Encode(option,data,output):
    loop = int(eval(_input % f"{tr} Encode Count : "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "lzm(data.encode('utf8')[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('lzma').decompress(__[::-1]);"
    elif option == 7:
        xx = "gzi(data.encode('utf8')[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('gzip').decompress(__[::-1]);"
    elif option == 8:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 9:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 10:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 11:
        xx = "b16(gzi(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('gzip').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 12:
        xx = "b32(gzi(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('gzip').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 13:
        xx = "b64(gzi(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('gzip').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 14:
        xx = "b16(lzm(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('lzma').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 15:
        xx = "b32(lzm(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('lzma').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 16:
        xx = "b64(lzm(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('lzma').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 17:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 18:
        xx = "gzi(mar(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__[::-1]));"
    elif option == 19:
        xx = "lzm(mar(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__[::-1]));"
    elif option == 20:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 21:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 22:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 23:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 24:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 25:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    elif option == 26:
        xx = "b16(lzm(mar(data.encode('utf8'))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 27:
        xx = "b32(lzm(mar(data.encode('utf8'))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 28:
        xx = "b64(lzm(mar(data.encode('utf8'))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('base64').b64decode(__[::-1])));"
    elif option == 29:
        xx = "b16(gzi(mar(data.encode('utf8'))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 30:
        xx = "b32(gzi(mar(data.encode('utf8'))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 31:
        xx = "b64(gzi(mar(data.encode('utf8'))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('base64').b64decode(__[::-1])));"
    elif option == 32:
        xx = "b16(zlb(lzm(mar(data.encode('utf8')))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1]))));"
    elif option == 33:
        xx = "b32(zlb(lzm(mar(data.encode('utf8')))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1]))));"
    elif option == 34:
        xx = "b64(zlb(lzm(mar(data.encode('utf8')))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))));"
    elif option == 35:
        xx = "b16(zlb(gzi(mar(data.encode('utf8')))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1]))));"
    elif option == 36:
        xx = "b32(zlb(gzi(mar(data.encode('utf8')))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1]))));"
    elif option == 37:
        xx = "b64(zlb(gzip(mar(data.encode('utf8')))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))));"
    elif option == 38:
        xx = "b16(zlb(lzm(gzi(mar(data.encode('utf8'))))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))));"
    elif option == 39:
        xx = "b32(zlb(lzm(gzi(mar(data.encode('utf8'))))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))));"
    elif option == 40:
        xx = "b64(zlb(lzm(gzi(mar(data.encode('utf8'))))))[::-1]"
        heading = "# Encoded By @MrEsfelurm | https://github/Mr-Spect3r\n\n_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))));"
    else:
        sys.exit("\n Invalid Option!")
    
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(f"{fls} TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(heading + data)
        f.close()


def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(lzm(gzi(mar(data.encode('utf8'))))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write("exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)


def MainMenu():
    try:
        clear()
        banner()
        menu()
        try:
            option = int(eval(_input % f"{tr} Option:{cn} "))
        except ValueError:
            sys.exit(f"\n{fls} Invalid Option !")
        
        if option > 0 and option <= 42:
            if option == 42:
                sys.exit(f"{tr} Thanks For Using this Tool")
            clear()
            banner()
        else:
            sys.exit(f'\n{fls} Invalid Option !')
        try:
            file = eval(_input % f"{tr} File Name : ")
            data = open(file).read()
        except IOError:
            sys.exit(f"\n{fls} File Not Found!")
        
        output = file.lower().replace('.py', '') + '_enc.py'
        if option == 41:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        print(f"\n{tr} Successfully Encrypted %s" % file)
        print(f"\n{tr} saved as %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()
