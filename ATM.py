username='sravya'
password='python123'

c_name=input("Enter your name:")
c_pass=str(input("Enter your password"))
if c_name==username and c_pass==password:
    print('''
          1.Deposit
          2.Withdraw
          3.ministatement
          4.exit
          ''')
    amount=50000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("Enter the amount"))
        amount+=dep
        print("Total amount:",amount)
    elif option==2:
        withd=int(input("Enter the amount:"))
        amount-=withd
        print("Total amount:",amount)  
    elif option==3:
        print("======ATM======")
        print("username:",username)
        print("Total amount:",amount)  
        print("Thanks for visiting") 
        print("============") 
    elif option==4:
        exit()  
else:
    print("please enter correct logins")    
    

