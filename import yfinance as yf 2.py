import yfinance as yf
# OPEN HIGH LOW CLOSE ADJCLOSE VOLUME
ticker = yf.Ticker('Googl').info
data=yf.download('googl','2022-01-01','2023-12-01')
#print(data)
a=data.to_numpy()

for i in range(0,100):
    o,h,l,c=a[i][0],a[i][1],a[i][2],a[i][3]
    if c>o and (o-l) >= 2*(c-o) and (h-c)<(c-o):
        print ("Hammer")
        o1,h1,l1,c1=a[i-1][0],a[i-1][1],a[i-1][2],a[i-1][3]
        if c>h1:
            print("Pattern is going to change!!")
    elif o>c and (c-l) >= 2*(o-c) and (h-o)<(o-c):
        print("Hangman")
   
    else:
        print("Not a Hangman")


