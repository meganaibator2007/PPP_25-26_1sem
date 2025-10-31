

if __name__ == "__main__":
    pass # Ваш код здесь
def apply_caesar(text: str, shift: int) -> str:
    """
    Применяет шифр Цезаря к строке.
    
    - Учитывает регистр (A-Z и a-z).
    - Сохраняет все остальные символы (цифры, знаки препинания) без изменений.
    - Корректно обрабатывает "заворачивание" (z -> a при c1, a -> z при c-1).
    """
    result = []
    for char in text:
        # 1. Обработка строчных букв (a-z)
        if 'a' <= char <= 'z':
            # Находим "базу" (код буквы 'a')
            base = ord('a')
            # (ord(char) - base) -> 0 для 'a', 1 для 'b', ... 25 для 'z'
            # (% 26) -> заворачивает сдвиг (26 % 26 = 0, 27 % 26 = 1, -1 % 26 = 25)
            new_ord = (ord(char) - base + shift) % 26 + base
            result.append(chr(new_ord))
        
        # 2. Обработка прописных букв (A-Z)
        elif 'A' <= char <= 'Z':
            base = ord('A')
            new_ord = (ord(char) - base + shift) % 26 + base
            result.append(chr(new_ord))
        
        # 3. Все остальные символы
        else:
            result.append(char)
            
    return "".join(result)

def apply_reverse(text: str) -> str:
    """
    Разворачивает строку задом наперед.
    """
    # [::-1] - это стандартный срез (slice) в Python для реверса
    return text[::-1]

def process_commands(initial_text: str, command_string: str) -> (list, str | None):
    """
    Пошагово применяет цепочку команд к строке и сохраняет историю.

    Возвращает кортеж:
    (history: list) - Список состояний строки, включая начальное.
    (error: str | None) - Сообщение об ошибке, если она произошла, иначе None.
    """
    
    # 1. Инициализация
    # history хранит все шаги. Начинаем с исходной строки.
    history = [initial_text]
    current_text = initial_text
    
    # Разбиваем строку команд "c1 r c-1" на список ["c1", "r", "c-1"]
    commands = command_string.split()

    # 2. Цикл обработки команд
    for cmd in commands:
        try:
            # --- Обработка команды "r" (Реверс) ---
            if cmd == 'r':
                current_text = apply_reverse(current_text)
            
            # --- Обработка команды "c" (Цезарь) ---
            elif cmd.startswith('c'):
                # Пытаемся получить число после 'c'
                shift_str = cmd[1:]
                
                # Проверка, что "c" не пустая (например, "c")
                if not shift_str:
                    raise ValueError("Команда 'c' требует числового сдвига (c1, c-2)")
                    
                shift = int(shift_str)
                current_text = apply_caesar(current_text, shift)
                
            # --- Место для расширения ---
            # Сюда можно легко добавить новые команды
            # elif cmd == 'd':
            #    current_text = apply_duplicate(current_text)
            # -------------------------------
                
            # --- Обработка неизвестной команды ---
            else:
                error_msg = f"Ошибка: Неизвестная команда '{cmd}'."
                print(error_msg)
                # Возвращаем историю до ошибки и саму ошибку
                return history, error_msg

            # Если этот шаг прошел успешно, добавляем результат в историю
            history.append(current_text)

        except ValueError:
            # Ошибка, если 'c' имеет неверный параметр (например, "c-a" или "c1.5")
            error_msg = f"Ошибка: Некорректный параметр для команды '{cmd}'."
            print(error_msg)
            return history, error_msg
        except Exception as e:
            # Любая другая непредвиденная ошибка
            error_msg = f"Критическая ошибка при выполнении '{cmd}': {e}"
            print(error_msg)
            return history, error_msg

    # 3. Успешное завершение
    # Все команды выполнены, возвращаем полную историю и отсутствие ошибки
    return history, None

# --- ПРИМЕР ИСПОЛЬЗОВАНИЯ ---

print("--- 1. Тест с примером из задания ---")
text1 = "abcd"
cmds1 = "c1 r c-1 r"
print(f"Исходная строка: '{text1}'")
print(f"Команды: '{cmds1}'")

# Запускаем обработку
history1, error1 = process_commands(text1, cmds1)

# Печатаем результат
print("\n📜 Пошаговая история изменений:")
for i, step in enumerate(history1):
    if i == 0:
        print(f"  Шаг 0 (Старт): '{step}'")
    else:
        print(f"  Шаг {i} (после {cmds1.split()[i-1]}): '{step}'")

if error1:
    print(f"\n❌ ОБРАБОТКА ПРЕРВАНА: {error1}")
else:
    print(f"\n✅ Результат: '{history1[-1]}'")


print("\n" + "="*40 + "\n")

print("--- 2. Тест с обработкой ошибок ---")
text2 = "Hello World!"
cmds2 = "c5 r c-a x1" # "c-a" - ошибка ValueError, "x1" - неизвестная команда
print(f"Исходная строка: '{text2}'")
print(f"Команды: '{cmds2}'")

history2, error2 = process_commands(text2, cmds2)

print("\n📜 Пошаговая история изменений:")
for i, step in enumerate(history2):
    if i == 0:
        print(f"  Шаг 0 (Старт): '{step}'")
    else:
        print(f"  Шаг {i} (после {cmds2.split()[i-1]}): '{step}'")

if error2:
    print(f"\n❌ ОБРАБОТКА ПРЕРВАНА: {error2}")
else:
    print(f"\n✅ Результат: '{history2[-1]}'")
