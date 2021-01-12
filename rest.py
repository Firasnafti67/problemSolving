a = 360//12
b = 360//60
m = 0.5
#  15 min -> 0.25 heure
#  x min -> 
def calculClock(hours,mins): 
    if(mins>=0 and mins<=59):
        hDegrees = (hours * 30) + (mins * 0.5)
        mDegrees = mins * 6
        diff = abs(hDegrees - mDegrees)
        if (diff > 180):
            diff = 360 - diff
        print("Résultat : ",+diff)

t = int(input())
while t:
  t = t-1
  x,y = map(int, input().split())
  calculClock(x,y)



