import random


class RC4:
    __S = [0]*256       ##状态向量
    __T = [0]*256       ##暂时向量
    __keylen = 256      ##密钥长度
    __key = []          ##可变长度密钥
    __keyStream = []    ##密钥流

    #初始化S,T,key
    def __init__(self,length):
        self.__keylen = length
        for i in range(self.__keylen):
            self.__key.append(random.randint(0,256))
        for i in range(0,256):
            self.__S[i] = i
            self.__T[i] = self.__key[i%self.__keylen]

    ##重新排列S
    def __rangeS(self):
        j = 0
        for i in range(0,256):
            j = (j+self.__S[i]+self.__T[i])%256
            self.__S[i],self.__S[j] = self.__S[j],self.__S[i]

    ##生成密钥流
    def __Stream(self,length):
        self.__rangeS()
        i,j=0,0
        for x in range(length):
            i = (i + 1) % 256
            j = (j + self.__S[i])%256
            self.__S[i],self.__S[j] = self.__S[j],self.__S[i]
            t = (self.__S[i] + self.__S[j]) % 256
            self.__keyStream.append(self.__S[t])


    def encrypt(self,pt):
        ct = ""
        ptlen = len(pt)
        bpt = []
        self.__Stream(ptlen)
        for i in pt:
            bpt.append(ord(i))
        for i in range(ptlen):
            char = bpt[i]^self.__keyStream[i]
            ct+=chr(char)
        print("ciphertext: "+ct)
        return ct

    def decrypt(self,ct):
        pt = ""
        ctlen = len(ct)
        cpt = []
        self.__Stream(ctlen)
        for i in ct:
            cpt.append(ord(i))
        for i in range(ctlen):
            char = cpt[i] ^ self.__keyStream[i]
            pt += chr(char)
        print("decryption: " + pt)
        return pt


if __name__ == '__main__':
    rc4 = RC4(16)
    while(True):
        plaintext = input("plaintext:  ")
        ciphertext = rc4.encrypt(plaintext)
        rc4.decrypt(ciphertext)
