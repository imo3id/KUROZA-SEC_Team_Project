import os
from scannerLogic import ScannerLogic
import Sniffing


def show_menu():
    print(f"\n{'=' * 30}")
    print("   SECURITY TOOLKIT - MAIN MENU")
    print(f"{'=' * 30}")
    print("1. Start Packet Sniffing (GUI)")
    print("2. Start Port Scanner (CLI)")
    print("3. Exit")
    print(f"{'=' * 30}")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("\n[!] Launching Packet Sniffer...")
            Sniffing.run_sniffer_ui()

        elif choice == '2':
            print("\n[!] Launching Port Scanner...")

            target_ip = input("Enter Target IP: ")
            ports_range = input("Enter Ports (e.g., 80,443 or 1-1000): ")

            try:

                scanner = ScannerLogic()

                # تحديث القيم داخل الـ args يدوياً لتخطي خطأ الـ Missing Arguments
                scanner.args.target = target_ip
                scanner.args.ports = ports_range

                # إعادة معالجة المنافذ بناءً على المدخل الجديد
                scanner.ports = scanner.parse_ports(ports_range)

                # تشغيل الفحص
                scanner.run()
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")


if __name__ == "__main__":
    main()