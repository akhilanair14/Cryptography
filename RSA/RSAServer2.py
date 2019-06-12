import socket;
import os;

socketServerName = "localhost"
socketServerPN = 7009
socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketServer.bind(('localhost',7009))
addr = (socketServerName, socketServerPN)
print ('server started')

def RSA_Decryption(CT):
    p = 613
    q = 827
    n = p*q
    Phi = (p-1)*(q-1)
    e = 535
    d = 16063
    value = 8
    Message = ''
    Parsed_Cipher = [CT[i:i+value] for i in range(0, len(CT),value)]
    for f in Parsed_Cipher:
        f = int(f)
        PlainExp = pow(f,d)
        PlainText = (PlainExp)%(n)
        Message += chr(PlainText)
    return Message

def RSA_Encryption(Reply):
    p = 613
    q = 827
    n = p*q
    Phi = (p-1)*(q-1)
    e = 535
    d = 16063
    Cipher_Reply = ''
    ASCII_Reply = [ord(i) for i in Reply]
    for c_reply in ASCII_Reply:
        CipherExp_Reply = pow(c_reply,e)
        CipherText_Reply = (CipherExp_Reply)%(n)
        CipherText_Reply = str(CipherText_Reply).zfill(8)
        Cipher_Reply = Cipher_Reply + CipherText_Reply
    return Cipher_Reply

while 1:
    CT, addr = socketServer.recvfrom(1024)                # using the recvfrom function the data and the address is stored in the Imagedata and addr variables                          
    print ('message received')
        

    PT = RSA_Decryption(CT)
    print "message is:",PT

    Reply = raw_input("type your reply: ")
    CT_Reply = RSA_Encryption(Reply)
    print "cipher of reply is:",CT_Reply
    
                                            
    socketServer.sendto(CT_Reply, addr)                   #send the packet to server if the above 'if' condition is not satisfied
    print ('the reply is sent')
    

socketServer.close()
