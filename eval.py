import numpy as np
details=dict()
details[12]=("Ayush","COA","CS","YES")
details[13]=("GS GREWAL","MATHS","CS","YES")
def add_book():
    isbn=int(input("Enter ISBN no. "))
    author=input("Enter author name ")
    title=input("Enter title ")
    genre=input("Enter title ")
    avai_status=input("Enter availibility status ")
    details[isbn]=dict(author=author,title=title,genre=genre,avai_status=avai_status)
    print(details)

def search_by_isbn():
    user_isbn=int(input("Enter ISBN no. "))
    for detail in details:
        if user_isbn==detail:
            print(detail)
 
                 
add_book()
search_by_isbn()
