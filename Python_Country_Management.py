# def display_menu():
#     print("\nMenu")
#     print("1) show database")
#     print("2) add item")
#     print("3) update item")
#     print("4) delete item")
#     print("5) exit")
    

# def show_database(countries):
#     print("country list:")
#     for index, country in enumerate(countries):
#         print(f"{index}:{country}")

# def add_item(countries):
#     country=input("enter the name of the country to add:")
#     if country in countries:
#         print("country already exists!")
#     else:
#         countries.append(country)
#         print(f"{country} has been added.")


# def update_item(countries):
#     show_database(countries)
#     try:
#         index=int(input("enter the index of the country to update:"))
#         if 0<=index<len(countries):
#             new_name=input("enter the new name:")
#             countries[index]=new_name
#             print("country updated successfully.")
#         else:
#             print("invalid index!")
#     except ValueError:
#         print("Please enter a valid number!")

# def delete_item(countries):
#     show_database(countries)
#     try:
#         index=int(input("enter the index of the country to delete:"))
#         if 0<=index<len(countries):
#             removed=countries.pop(index)
#             print(f"{removed} has been deleted.")
#         else:
#             print("Invalid index.")
#     except ValueError:
#         print("Please enter a valid number!")

# def main():
#     countries=["India","United Kingdom","Germany","France","Spain"]
#     print("current database is:")
#     # show_database(countries)
#     while True:
#         display_menu()
#         choice=input("enter your choice:")
#         if choice=='1':
#             show_database(countries)
#         elif choice=='2':
#             add_item(countries)
#         elif choice=='3':
#             update_item(countries)
#         elif choice=='4':
#             delete_item(countries)
#         elif choice=='5':
#             print("exiting program.")
#             break
#         else:
#             print("invalid choice. please select a valid option.")


# main()









          
import pyodbc
conn=pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    # 'DRIVER={ SQL Server C};'
    'SERVER=localhost\\SQLEXPRESS;'
    # 'SERVER=CO3168\SQLEXPRESS;'
    'DATABASE=CountryDB;'
    'Trusted_Connection=yes;')
cursor=conn.cursor()

def display_menu():
    print("\nMenu")
    print("1) show database")
    print("2) add item")
    print("3) update item")
    print("4) delete item")
    print("5) exit")
    

def show_database():
    cursor.execute("select * from Countries")
    countries=cursor.fetchall()
    print("country list:")
    for country in countries:
        print(f"{country.ID}: {country.CountryName}")

def add_item():
    country=input("enter the name of the country to add:")
    cursor.execute("insert into Countries(CountryName) values (?)",(country,))
    conn.commit()
    print(f"{country} has been added.")
        


def update_item():
    show_database()
    try:
        country_id=int(input("enter the ID of the country to update:"))
        new_name=input("enter the new name:")
        cursor.execute("update Countries set CountryName=? where ID=?",(new_name,country_id))
        conn.commit()
        print("country updated successfully.")
            
    except ValueError:
        print("Please enter a valid ID!")

def delete_item():
    show_database()
    try:
        country_id=int(input("enter the ID of the country to delete:"))
        cursor.execute("delete from Countries where ID=?",(country_id,))
        conn.commit()
        print("country deleted successfully.")
    except ValueError:
        print("Please enter a valid ID!")



def main():
    
    while True:
        display_menu()
        choice=input("enter your choice:")
        if choice=='1':
            show_database()
        elif choice=='2':
            add_item()
        elif choice=='3':
            update_item()
        elif choice=='4':
            delete_item()
        elif choice=='5':
            print("exiting program.")
            conn.close()
            break
        else:
            print("invalid choice. please select a valid option.")


main()
print("This is a remote change in NewProjectFolder")
































































