pontok = []
sorok = 0
with open("04.13/pontok.txt","r",encoding="utf-8")as f:
    for i in f:
        pontok.append(i.strip().split(";"))
        sorok += 1
eredmeny = int(pontok[0][1])
for i in range(1,sorok):
    eredmeny = eredmeny + int(pontok[i][1])
legm_pont = int(pontok[0][1])
legj_tan = pontok[0][0]
for i in range(0,sorok):
    if int(pontok[i][1]) > legm_pont:
        legm_pont = int(pontok[i][1])
        legj_tan = pontok[i][0]
eredmeny = eredmeny / sorok
print(f"Az osztály átlaga: {eredmeny}")
print(f"A legjobb eredményt elérte: {legj_tan,legm_pont} pont")
print(f"60 pont alatti tanulók:")
for i in range(0,sorok):
    if int(pontok[i][1]) < 60:
        print(pontok[i][0],"-",pontok[i][1],"pont")
with open("04.13/elegtelenek.txt","w",encoding="utf-8")as c:
    c.write(f"60 pont alatti tanulók:")
    c.write("\n")
    for i in range(0,sorok):
        if int(pontok[i][1]) < 60:
            c.write(pontok[i][0])
            c.write(" - ")
            c.write(pontok[i][1])
            c.write("\n")