import os
from IPGenerator import generate_ip_range, generate_ips, save_ips_to_file

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menu Utama:")
        print("1. Batasi Generate IP")
        print("2. Generate seluruh IP")
        choice = input("Pilih menu (1/2) atau 'q' untuk keluar: ")

        if choice == 'q':
            break
        elif choice == '1':
            total_ips = int(input("\nBerapa IP yang ingin dibuat: "))
            randomize = input("Generate IP Random (yes/no): ").strip().lower() == 'yes'
            ip_range_choice = input("Generate IP Range (yes/no): ").strip().lower() == 'yes'

            if ip_range_choice:
                start_ip = input("Masukkan IP awal (example: 10.10.10.10): ").strip()
                end_ip = input("Masukkan IP akhir (example: 20.20.20.20): ").strip()
                ip_list = generate_ip_range(start_ip, end_ip, total_ips, randomize)
            else:
                ip_list = generate_ips(total_ips, randomize)

            filename = input("\nMasukkan nama file untuk menyimpan (example: ip_addresses.txt): ").strip()
            save_ips_to_file(filename, ip_list)
            input(f"\n{total_ips} IP telah disimpan dalam Result/{filename}")
        
        elif choice == '2':
            print("1. Generate IP Random")
            print("2. Generate IP Sort ascending or descending")
            sub_choice = input("Pilih submenu (1/2): ")

            if sub_choice == '1':
                ip_list = generate_ips(4294967296, True)
            elif sub_choice == '2':
                order = input("Pilih urutan (ascending/descending): ").strip().lower()
                ip_list = [f"{a}.{b}.{c}.{d}" for a in range(256) for b in range(256) for c in range(256) for d in range(256)]
                if order == 'descending':
                    ip_list.reverse()
            
            filename = input("Masukkan nama file untuk menyimpan (example: ip_addresses.txt): ").strip()
            os.system('cls' if os.name == 'nt' else 'clear')
            save_ips_to_file(filename, ip_list)
            input(f"Seluruh IP telah disimpan dalam Result/{filename}")

if __name__ == "__main__":
    main()
