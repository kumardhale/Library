import mysql.connector as a
con = a.connect(host="localhost",user="root",passwd="1234",database="library")

def addbook():
    bn=input("Enter a Book name:")
    c=input("Enter a Book code:")
    t=input("Total Books:")
    s=input("Enter Subject:")
    data=(bn,c,t,s)
    sql='insert into books values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Succesfully")
    main()

def issuebook():
    n=input("Enter Name:")
    r=input("Enter a Reg No:")
    co=input("Enter Book code:")
    d=input("Enter Date:")
    a="insert into issue values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("Book issued to:",n)
    bookup(co,-1)

def submitbook():
    n=input("Enter Name:")
    r=input("Enter a Reg No:")
    co=input("Enter Book code:")
    d=input("Enter Date:")
    a="insert into submit values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("Book submitted from:",n)
    bookup(co,1)

def bookup(co,u):
    a="select TOTAL from books where BCODE=%s"
    data=(co,)
    c=con.curser()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL =%s where BCODE=%s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()

def deletebook():
    ac=input("Enter Book code:")
    a="delete from books where BCODE=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()


def displaybook():
    a="select * from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book name:",i[0])
        print("Book code:",i[1])
        print("Total:",i[2])
    main()

def main():
    print("""
                        LIBRARY MANAGER
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.DISPLAY BOOKS
    """)
    choice=input("Enter Task No:")
    if choice=='1':
        addbook()
    elif choice=='2':
        issuebook()
    elif choice=='3':
        submitbook()
    elif choice=='4':
        deletebook()
    elif choice=='5':
        displaybook()
    else:
        print("wrong choice")
        main()

def pswd():
    ps=input("Enter password:")
    if ps=="kumar":
        main()
    else:
        print("wrong Password")
        pswd()
pswd()

        
        
        
































































