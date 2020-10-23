# import modules
import mysql.connector
import os

# connect modules to db
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_mainan"
)

# CRUDS functions
def insert_data(db):
    name = input("Masukkan Nama :")
    age = input("Masukkan Umur : ")
    address = input("Masukkan Alamat : ")

    cursor = db.cursor()

    sql = "INSERT INTO customers (name, age, address) VALUES (%s,%s,%s)"
    val = (name, age, address)
    cursor.execute(sql, val)

    db.commit()

    print(f"{cursor.rowcount} data berhasil ditambahkan")

def select_data(db):
    cursor = db.cursor()
    sql="SELECT * FROM customers"
    cursor.execute(sql)

    result = cursor.fetchall()
    for data in result:
        print(data)

def update_data(db):
    customer_id = input("Masukkan ID yang ingin diganti :")
    name = input("Masukkan Nama Baru:")
    age = input("Masukkan Umur Baru: ")
    address = input("Masukkan Alamat Baru: ")

    cursor = db.cursor()

    sql = "UPDATE customers set name=%s, age=%s, address=%s WHERE customer_id = %s"
    val = (name, age, address, customer_id)
    cursor.execute(sql, val)

    db.commit()

    print(f"{cursor.rowcount} data berhasil diubah")

def delete_data(db):
    customer_id = input("Masukkan Id yang ingin dihapus :")
    
    cursor = db.cursor()

    sql="DELETE FROM customers WHERE customer_id = %s"
    val =(customer_id,)
    cursor.execute(sql, val)

    db.commit()

    print(f"{cursor.rowcount} data berhasil dihapus")

def search_data(db):
    keyword = input("Masukkan keyword :")

    cursor = db.cursor()
    sql ="SELECT * FROM customers WHERE name LIKE %s"
    val = (f"%{keyword}%",)

    cursor.execute(sql, val)
    result = cursor.fetchall()

    if cursor.rowcount <= 0:
        print("Data tidak ditemukan")
    else:
        for data in result:
            print(data)

# GUI Menu
def menu(db):
    print("             APLIKASI CRUDS GUI ")
    print("=================================================")
    menu_list = ["1. Lihat Data", "2. Cari Data", "3. Tambah Data", "4. Edit Data", "5. Hapus Data", "0. Keluar"]
    for m in menu_list:
        print(m)

    menu_input = input("Pilih Menu :")

    if menu_input == "1":
        select_data(db)
    elif menu_input == "2":
        search_data(db)
    elif menu_input == "3":
        insert_data(db)
    elif menu_input == "4":
        update_data(db)
    elif menu_input == "5":
        delete_data(db)
    elif menu_input == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == '__main__':
    while (True):
        menu(db)