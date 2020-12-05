import socket


host = "localhost"
port = 8887
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket oluşturuldu")

    s.bind((host, port))
    print("socket {} nolu porta bağlandı".format(port))

    s.listen(5)
    print("socket dinleniyor")
except socket.error as msg:
    print("Hata:",msg)

while True:


   c, addr = s.accept()
   print('Gelen bağlantı:', addr)
   ad=input("Kullanıcı adınızı girin>")
   c.send(ad.encode('utf-8'))
   ad2= c.recv(1024)
   print("Bağlantı gelen kişi:",ad2.decode("utf-8"))
   while  True:
        mesaj = input("Mesajınızı Girin>")
        if mesaj =="q":
          break
          
        c.send(mesaj.encode('utf-8'))
        print(ad,">",mesaj)
        yanıt= c.recv(1024)
        print(ad2,">",yanıt.decode("utf-8"))



   c.close()
