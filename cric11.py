import time
toporder=[]
toporderbat=[]

wlcm='''
        CricXI - 'You are the COACH'
'''

for wlcmvariable in wlcm:
    print(wlcmvariable,end="")
    time.sleep(0.033)
    
print('''
____________
            |
[1] START   |
[2] CREDITS |
[3] QUIT    |
____________|
''')


initchoice=int(input("Enter Your Choice -> "))

if initchoice==3:
    exit()
    
if initchoice==2:
    while 2<3:
        print("linuxistliebe-",end="")


if initchoice==1:
    print()
    print("Welcome Mr.Coach")
    print('''
[1] TOP ORDER Menu
[2] MIDDLE ORDER Menu
[3] LOWER ORDER Menu
[4] CAPTAINCY Options
[5] Jackie-Moggy Trophy
''')

    choice=int(input("Enter Your Choice -> "))
    if choice==1:
        print()
        print("-TOP ORDER-")
        for i in range(3):
            nmbtsmn=input("Enter The Name Of Batsman -> ")
            toporder.append(nmbtsmn.title())
            
        print("(@) Top Order Batsman are -",toporder)
        

    
