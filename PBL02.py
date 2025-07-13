import sqlite3

#untuk koneksi ke database
koneksi = sqlite3.connect('P01201.db')
cur = koneksi.cursor()

#untuk membuat tabel
cur.execute('''
CREATE TABLE IF NOT EXISTS drinks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')
koneksi.commit()

#fungsi untuk create data
def create_drink():
    name = input("Masukkan nama minuman: ")
    price = float(input("Masukkan harga minuman: "))
    stock = int(input("Masukkan stok minuman: "))
    cur.execute("insert into drinks (name, price, stock) values (?, ?, ?)", (name, price, stock))
    koneksi.commit()
    print("Minuman berhasil ditambahkan.")
    
#fungsi untuk read data
def read_drinks():
    print("Daftar Minuman:")
    for row in cur.execute("SELECT * FROM drinks"):
        print(f"ID: {row[0]}, Nama: {row[1]}, Harga: {row[2]}, Stok: {row[3]}")
        
#fungsi untuk update data
def update_drink():
    read_drinks()
    drink_id = int(input("Masukkan ID minuman yang ingin diupdate: "))
    name = input("Masukkan nama baru minuman: ")
    price = int(input("Masukkan harga baru minuman: "))
    stock = int(input("Masukkan stok baru minuman: "))
    cur.execute("UPDATE drinks SET name = ?, price = ?, stock = ? WHERE id = ?", (name, price, stock, drink_id))
    koneksi.commit()
    print("Minuman berhasil diupdate.")
    
#fungsi untuk delete data
def delete_drink():
    read_drinks()
    drink_id = int(input("Masukkan ID minuman yang ingin dihapus: "))
    cur.execute("DELETE FROM drinks WHERE id = ?", (drink_id,))
    koneksi.commit()
    print("Minuman berhasil dihapus.")
    
#fungsi untuk search data
def search_drink():
    name = input("Masukkan nama minuman yang ingin dicari: ")
    cur.execute("SELECT * FROM drinks WHERE name LIKE ?", ('%' + name + '%',))
    results = cur.fetchall()
    if results:
        print("Hasil Pencarian:")
        for row in results:
            print(f"ID: {row[0]}, Nama: {row[1]}, Harga: {row[2]}, Stok: {row[3]}")
    else:
        print("Minuman tidak ditemukan.")
        
#menu utama
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Minuman")
        print("2. Lihat Daftar Minuman")
        print("3. Update Minuman")
        print("4. Hapus Minuman")
        print("5. Cari Minuman")
        print("6. Keluar")
        
        choice = input("Pilih opsi (1-6): ")
        
        if choice == '1':
            create_drink()
        elif choice == '2':
            read_drinks()
        elif choice == '3':
            update_drink()
        elif choice == '4':
            delete_drink()
        elif choice == '5':
            search_drink()
        elif choice == '6':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            
main_menu()