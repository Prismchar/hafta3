import random

FB_gol=random.randint(0,5)
GS_gol=random.randint(0,5)

print("GS gol sayısı:", GS_gol)
print("FB gol sayısı:", FB_gol)

if GS_gol > FB_gol:
    print("Galatasaray kazandı")
elif GS_gol == FB_gol:
    print("Beraberlik")
else:
    print("Fenerbahçe kazandı")


