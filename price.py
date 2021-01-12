price=[50,55,20,15,80,40,50,60,5,20,70,30,45,30,35,80,20,55,50,55,45,65,40,60,40,58,20,35,90,55]
min = 0
max = 0
for i in range(len(price)):
    if (price[i]>price[max]):
        max = i
    if (price[i]<price[min]):
        min = i
print("J_achat ",max + 1," J_vente ",min + 1)