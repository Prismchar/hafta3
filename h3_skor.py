import random

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
$echo "# hafta3" >> h3_skor.py
$git init
$git add h3.skor.py
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Prismchar/hafta3.git
git push -u origin main

