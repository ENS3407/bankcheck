bakiye= 1000

x=int(input("Yatırım mı Çekme mi- Yatırım için 1 çekim için 2"))

if x ==1 :
  yatirim=int(input("ne kadar yatırmak istersiniz"))
  bakiye=bakiye+yatirim
  print( "Yeni Bakiyeniz: " + str(bakiye))
  
elif x == 2:
  cekim=int(input("ne kadar çekmek istersiniz"))
  if x <= bakiye:
    print("Bakiyeniz Yetersiz")
    
  bakiye=bakiye-cekim
  
  
else:
  print("hatalı giriş")
  




