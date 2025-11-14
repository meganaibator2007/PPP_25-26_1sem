

if __name__ == "__main__":
    def apply_caesar(text: str, shift: int) -> str:
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                base = ord('a')
                new_ord = (ord(char) - base + shift) % 26 + base
                result.append(chr(new_ord))
            
            elif 'A' <= char <= 'Z':
                base = ord('A')
                new_ord = (ord(char) - base + shift) % 26 + base
                result.append(chr(new_ord))
            
            else:
                result.append(char)
                
        return "".join(result)
    
    def apply_reverse(text: str) -> str:
        return text[::-1]
    
    def process_commands(initial_text: str, command_string: str) -> (list, str | None):
        
        history = [initial_text]
        current_text = initial_text
        
        commands = command_string.split()
    
        for cmd in commands:
            try:
                if cmd == 'r':
                    current_text = apply_reverse(current_text)
                
                elif cmd.startswith('c'):
                    shift_str = cmd[1:]
                    
                    if not shift_str:
                        raise ValueError("Команда 'c' требует числового сдвига (c1, c-2)")
                        
                    shift = int(shift_str)
                    current_text = apply_caesar(current_text, shift)
                    
                else:
                    error_msg = f"Ошибка: Неизвестная команда '{cmd}'."
                    print(error_msg)
                    return history, error_msg
    
                history.append(current_text)
    
            except ValueError:
                error_msg = f"Ошибка: Некорректный параметр для команды '{cmd}'."
                print(error_msg)
                return history, error_msg
            except Exception as e:
                error_msg = f"Критическая ошибка при выполнении '{cmd}': {e}"
                print(error_msg)
                return history, error_msg
    
        return history, None
    
    print("--- 1. Тест с примером из задания ---")
    text1 = "abcd"
    cmds1 = "c1 r c-1 r"
    print(f"Исходная строка: '{text1}'")
    print(f"Команды: '{cmds1}'")
    
    history1, error1 = process_commands(text1, cmds1)
    
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
    cmds2 = "c5 r c-a x1"
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
