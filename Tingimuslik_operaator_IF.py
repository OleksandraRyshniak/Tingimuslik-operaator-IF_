import random
from datetime import datetime


# 1. 
a=str(input("Sisestage nimi: "))
nimi=a.isupper()
if nimi==True:
    print ("Läheme kinno.")
    b=input("Sisestage vanus: ")
    if b.isdigit():
        b=int(b)
    if b<6:
        print("Tasuta.")
    elif 6<=b<=14:
        print("Lastepilet.")
    elif 15<=b<=65:
        print("Täispilet")
    elif b<65:
         print("Sooduspilet.")
    elif b<0 or b>100:
         print("Viga andmetega.")
    else:
        print("Sisestage täisarv.")
else:
    print ("Ei lähe kinno.")

#2. 
nimi_1=input("Sisesta eesnimi: ")
n=nimi_1.isalpha()
nimi_2=input("Sisestage nimi: ")
ni=nimi_2.isalpha()
if n==True and ni==True:
    print(f"Täna on {nimi_1} ja {nimi_2} lauakaaslased.")
else: 
    print("Viga!")


# 3.
a=float(input("Ruumi pikkus: "))
b=float(input("Ruumi laius: "))
S=a*b
r=input("Kas soovite teha renoveerimist?")
if r=="Jah":
    c=float(input("Kui palju maksab ruutmeeter?"))
summ=S*c
print(f"Põranda väljavahetamine maksab: {summ}")

#4 
a=float(input("Sisestage alghind: "))
if a>700:
    b=a*0.3
    hind=a-b
    print(f"Soodushind: {hind}")
else:
    print("Sellele summale ei kohaldata allahindlust.")

# 5 
a=float(input("Milline on temperatuur praegu: "))
if a>18:
    print("Kõrge temperatuur")
else:
    print("OK")

# 6 
a=float(input("Kui pikk sa oled: "))
if a<=160:
    print("Madal kasvu.")
elif 160<a<180:
    print("Keskmine pikkus")
elif 180<a:
    print("Kõrge kasvu")
else:
    print("Viga!")

# 7 
a=float(input("Kui pikk sa oled: "))
b=input("Mis soost sa oled?")
if a<=160:
    print("Madal kasvu.")
elif 160<a<180:
    print("Keskmine pikkus")
elif 180<a:
    print("Kõrge kasvu")
else:
    print("Viga!")

# 8 
a = input("Kas soovite osta leiba? ")
if a == "Jah":
    b = random.randint(1, 10)
    print(f"Hind: {b} eurot.")
    c = input("Kui palju tükki? ")
    if c.isdigit(): 
        c = int(c)
        summ = b * c
    else:
        print("Viga: Palun sisestage korrektne kogus.")
p = input("Kas soovite osta piim? ")
if p == "Jah":
    hind = random.randint(1, 10)  
    print(f"Hind: {hind} eurot.")
    d = input("Kui palju tükki? ")
    if d.isdigit():
        d = int(d)
        summ1 = hind * d
    else:
        print("Viga: Palun sisestage korrektne kogus.")
t = input("Kas soovite osta mahl? ")
if t == "Jah":
    hind_ = random.randint(1, 10)  
    print(f"Hind: {hind_} eurot.")
    l = input("Kui palju tükki? ")
    if l.isdigit():
        l = int(l)
        summ2 = hind_ * l
    else:
        print("Viga: Palun sisestage korrektne kogus.")
summ_ = summ + summ1 + summ2
print(f"Tšeki summa: {summ_} eurot.")


# 9 
a=int(input("Sisestage külg: "))
b=int(input("Sisestage külg: "))
if a==b:
    print("See on kvadraat.")
else:
    print("See ei ole kvadraat.")

# 10 
a=float(input("Sisestage arv: "))
b=float(input("Sisestage arv: "))
i=input("Millist operatsiooni soovite teostada?")
if i=="+":
    summ=a+b
    print(f"Summa on võrdne: {summ} ")
elif i=="-":
    s=a-b
    print(f"Lahutamine on võrdne: {s} ")
elif i=="*":
    d=a*b
    print(f"Korrutamine võrdub: {d}")
elif i=="/":
    v=a/b
    print(f"Osakond võrdub: {v}")
else:
    print("Viga!")

#11
a = input("Sisestage oma sünniaeg (dd.mm.yyyy): ")
a = datetime.strptime(a, "%d.%m.%Y")  
today = datetime.today()  
if a.day == today.day and a.month == today.month:
    print("Palju õnne sünnipäevaks!!!")
else:
    print("See ei ole sinu sünnipäev.")


# 12 
hind=float(input("Kauba hind: "))
if hind<10:
    a=hind*0.1
    hind_=hind-a
    print(f"Toote lõplik hind: {hind_}")
elif hind>10:
    b=hind*0.2
    hind1=hind-b
    print(f"Toote lõplik hind: {hind1}")
else:
    print("Viga!")

# 13 Футбольная команда
# Вам необходимо создать программу, которая проверит, подходит ли кандидат для данной команды.
# Возраст должен быть от 16 до 18 лет, допускаются только лица мужского пола.
# Улучшить программу таким образом, чтобы если заявитель — женщина, то вопрос о возрасте вообще не задавался.
# 14
# Автобусная логистика

# Допустим, нам нужно перевезти определенное количество людей в автобусах с определенным количеством мест. 
# Сколько автобусов понадобится, чтобы доставить всех, 
# и сколько человек будет в последнем автобусе (при условии, что все предыдущие полностью заполнены)? 
# Напишите программу, которая запрашивает количество людей и размер автобусов, а затем решает эту задачу.
