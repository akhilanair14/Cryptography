import socket;
import os;

socketServerName = "localhost"
socketServerPN = 7009
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (socketServerName, socketServerPN)
print('client started')

def RSA_Encryption(Text):
    p = 613
    q = 827
    n = p*q
    Phi = (p-1)*(q-1)
    e = 535
    d = 16063
    Cipher = ''
    ASCII_Message = [ord(i) for i in Text]
    for c in ASCII_Message:
        CipherExp = pow(c,e)
        CipherText = (CipherExp)%(n)
        CipherText = str(CipherText).zfill(8)
        Cipher = Cipher + CipherText
    return Cipher

def RSA_Decryption(CT_Reply):
    p = 613
    q = 827
    n = p*q
    Phi = (p-1)*(q-1)
    e = 535
    d = 16063
    value = 8
    Reply = ''
    Parsed_Cipher = [CT_Reply[i:i+value] for i in range(0, len(CT_Reply),value)]
    for f in Parsed_Cipher:
        f = int(f)
        PlainExp = pow(f,d)
        PlainText = (PlainExp)%(n)
        Reply += chr(PlainText)
    return Reply

while 1:
    Text = raw_input("Enter the message: ")
    CT = RSA_Encryption(Text)
    print "cipher is:",CT

    socketClient.sendto(CT, addr)                   #send the packet to server if the above 'if' condition is not satisfied
    print ('the message is sent')

    
    CT_Reply, addr = socketClient.recvfrom(1024)                # using the recvfrom function the data and the address is stored in the Imagedata and addr variables                          
    print ('message received')

    PT = RSA_Decryption(CT_Reply)
    print "message is:",PT
    

socketClient.close()
