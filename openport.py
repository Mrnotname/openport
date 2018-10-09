#!usr/bin/python

import socket
def banner():
     print ("\033[93m ||==========================||")
     print ("\033[93m ||=====CEK PORT TERBUKA=====||")
     print ("\033[94m ||======TOOL'S SCAN PORT====||")
     print ("\033[91m ||=====coding by MR.ID======||")
     print ("\033[94m ||===TEAM PASUKAN TERMUX====||")
     print ("\033[93m ||=======BEST TO ===========||")
     print ("\033[91m ||=======B4CKD00R CR45H=====||")
     print ("\033[93m ||==========================||")
def scan():
    server = raw_input("\033[94m Masukkan alamat server:")
    ip = socket.gethostbyname(server)
    print "Alamat IP server pada:",ip
    for port in range(1,1025):
        konek = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        hasil = konek.connect_ex((ip,port))
        if hasil == 0:
            print "Port terbuka pada: [{}]".format(port)
        konek.close()
           
banner()
scan()
