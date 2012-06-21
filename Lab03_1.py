#archibold_acheampong

i=1
x = int(input("Enter the number:"))
counter = 0
while True:
    c=0;
    for j in range (1, (i+1), 1):
        a = i%j
        if (a==0):
            c = c+1
    if (c==2):
        print (i),
        if counter==10:
            print
        if counter==20:
            print
        if counter==30:
            print
        if counter==40:
            print
        if counter==50:
            print
        #if counter%10==0:
         #   print
        counter = counter + 1
        if counter >= x:
            break
    i=i+1
