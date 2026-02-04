import sys
import os
import shlex

# Ensure the current directory is in the path for module importing
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    import Sniffing
    from scannerLogic import ScannerLogic
except ImportError as e:
    print(f"⚠️ Import Error: {e}")
    sys.exit()


def main():
    while True:
        print("\n" + "=" * 45)
        print("        🛡️  KUROZA-SEC NETWORK TOOLBOX")
        print("=" * 45)
        print(" [1] Run Packet Sniffing Tool (GUI)")
        print(" [2] Run Port Scanner Tool (CLI)")
        print(" [0] Exit")
        print("-" * 45)

        choice = input("Select an option (0-2): ").strip()

        match choice:
            case "1":
                print("\n[+] Launching Packet Sniffer Interface...")
                try:
                    Sniffing.run_sniffer_ui()
                except Exception as e:
                    print(f"❌ Error starting Sniffer: {e}")

            case "2":
                print("\n--- Port Scanner Configuration ---")
                target = input("Target IP (required): ").strip()
                if not target:
                    print("⚠️ Error: Target IP is required.")
                    continue

                ports = input("Port range [default 1-1024]: ").strip() or "1-1024"
                threads = input("Number of threads [default 100]: ").strip() or "100"
                output = input("Output file name (optional): ").strip()

                # بناء قائمة الوسائط (sys.argv) لمحاكاة سطر الأوامر
                # نضع اسم الملف كأول عنصر، ثم الهدف، ثم الخيارات
                args_list = [sys.argv[0], target, "-p", ports, "-t", threads]

                if output:
                    args_list.extend(["-o", output])

                # تحديث sys.argv فعلياً ليقوم موديول argparse بقراءتها
                sys.argv = args_list

                print(f"\n[+] Initializing Scanner for {target}...")
                try:
                    # الآن سيقوم ScannerLogic باستدعاء get_arguments()
                    # وسيجد كافة البيانات التي أدخلتها في sys.argv
                    scanner = ScannerLogic()
                    scanner.run()
                except Exception as e:
                    print(f"❌ Error starting Scanner: {e}")

            case "0":
                print("👋 Shutting down... Goodbye!")
                break
            case _:
                print("⚠️ Invalid selection. Please choose 1, 2, or 0.")


if __name__ == "__main__":
    main()