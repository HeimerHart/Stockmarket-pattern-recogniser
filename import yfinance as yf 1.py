import yfinance as yf
# OPEN HIGH LOW CLOSE ADJCLOSE VOLUME
ticker = yf.Ticker('Googl').info
data=yf.download('googl','2023-01-01','2023-12-01')
#print(data)
a=data.to_numpy()




# Hammer hangman identifier
def ham(o,h,l,c):
   if c>o and (o-l) >= 2*(c-o) and (h-c)<(c-o):
      print ("Hammer")

   elif o>c and (c-l) >= 2*(o-c) and (h-o)<(o-c):
      print("Hangman")
   
   else:
      print("Not a Hangman")
#print(a[2][2]*10)
for i in range(0,100):
   ham(a[i][0],a[i][1],a[i][2],a[i][3])

