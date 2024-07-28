import argparse
from pathlib import Path
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширеннями.")
    parser.add_argument("--source", type=Path, help="Шлях до вихідної директорії")
    parser.add_argument("--dest", type=Path, help="Шлях до директорії призначення")
    return parser.parse_args()

def copy_files(src, dst):
    try:
        for item in src.iterdir():
            if item.is_dir():
                # Рекурсивний виклик для піддиректорії
                copy_files(item, dst)
            else:
                # Визначення розширення файлу та створення піддиректорії
                file_extension = item.suffix[1:]  # отримуємо розширення файлу без крапки
                target_dir = dst / file_extension
                target_dir.mkdir(parents=True, exist_ok=True)
                
                # Визначення цільового шляху
                target_file = target_dir / item.name
                
                # Перевірка наявності файлу з таким ім'ям
                counter = 1
                while target_file.exists():
                    # Додавання суфіксу до імені файлу, щоб уникнути конфліктів
                    target_file = target_dir / f"{item.stem}_{counter}{item.suffix}"
                    counter += 1
                
                # Копіювання файлу
                shutil.copy(item, target_file)
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def main():
    args = parse_args()
    
    # Якщо аргументи не передані, запросити їх через input
    if not args.source:
        args.source = Path(input("Введіть шлях до вихідної директорії: "))
    if not args.dest:
        args.dest = Path(input("Введіть шлях до директорії призначення (або натисніть Enter для використання 'dist'): ") or "dist")
    
    print(f"Вихідна директорія: {args.source}")
    print(f"Директорія призначення: {args.dest}")
    
    # Створюємо директорію призначення, якщо вона не існує
    args.dest.mkdir(parents=True, exist_ok=True)
    copy_files(args.source, args.dest)

if __name__ == "__main__":
    main()
