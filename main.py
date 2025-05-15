from use_cases.fruit_usecase import FruitUseCases
from infrastructure.in_memory_repo import InMemoryFruitRepository

def menu(usecase):
    while True:
        print("\n1. Tambah Buah\n2. Lihat Semua Buah\n3. Lihat Buah by ID\n4. Edit Buah\n5. Hapus Buah\n6. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            name = input("Nama Buah: ")
            price = float(input("Harga Buah: "))
            fruit = usecase.add(name, price)
            print(f"Buah {fruit.name} berhasil ditambahkan dengan ID {fruit.id}.")

        elif choice == "2":
            fruits = usecase.browse()
            if fruits:
                for fruit in fruits:
                    print(f"ID: {fruit.id} | Nama: {fruit.name} | Harga: {fruit.price}")
            else:
                print("Belum ada buah yang ditambahkan.")

        elif choice == "3":
            fruit_id = int(input("Masukkan ID Buah: "))
            fruit = usecase.read(fruit_id)
            if fruit:
                print(f"ID: {fruit.id} | Nama: {fruit.name} | Harga: {fruit.price}")
            else:
                print("Buah tidak ditemukan.")

        elif choice == "4":
            fruit_id = int(input("Masukkan ID Buah yang ingin diedit: "))
            name = input("Nama Baru: ")
            price = float(input("Harga Baru: "))
            updated = usecase.edit(fruit_id, name, price)
            if updated:
                print(f"Buah berhasil diupdate: {updated.name} | Harga: {updated.price}")
            else:
                print("Buah tidak ditemukan.")

        elif choice == "5":
            fruit_id = int(input("Masukkan ID Buah yang ingin dihapus: "))
            deleted = usecase.delete(fruit_id)
            print("Buah berhasil dihapus." if deleted else "Buah tidak ditemukan.")

        elif choice == "6":
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    repo = InMemoryFruitRepository()
    usecase = FruitUseCases(repo)
    menu(usecase)
