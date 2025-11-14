

if __name__ == "__main__":
    pass # Ваш код здесь
import pprint

def generirovat_perestanovki(elementy, logger):
    itogovye_perestanovki = []
    elementy_list = list(elementy) 
    
    logger.append("--- СТАРТ: Генерация ПЕРЕСТАНОВОК ---")
    logger.append(f"Входные элементы: {elementy_list}")
    
    rekursiya_perestanovok(
        dostupnye=elementy_list,
        tekushiy_put=[],
        itogovye_perestanovki=itogovye_perestanovki,
        logger=logger,
        uroven=0
    )
    
    logger.append("--- КОНЕЦ: Генерация ПЕРЕСТАНОВОК ---")
    return itogovye_perestanovki

def rekursiya_perestanovok(dostupnye, tekushiy_put, itogovye_perestanovki, logger, uroven):
    indent = "  " * uroven
    
    logger.append(f"{indent}--- Вызов (уровень {uroven}) ---")
    logger.append(f"{indent}Доступные элементы: {dostupnye}")
    logger.append(f"{indent}Частичный результат (текущий путь): {tekushiy_put}")

    if not dostupnye:
        logger.append(f"{indent}!!! РЕЗУЛЬТАТ: {tekushiy_put} (Добавляем в итог)")
        itogovye_perestanovki.append(tekushiy_put.copy())
        logger.append(f"{indent}--- Возврат (базовый случай) ---")
        return

    for i in range(len(dostupnye)):
        
        vybranniy = dostupnye[i]
        
        novye_dostupnye = dostupnye[:i] + dostupnye[i+1:]
        
        tekushiy_put.append(vybranniy)
        
        logger.append(f"{indent}-> Шаг: Выбираем '{vybranniy}'. Путь: {tekushiy_put}. Остались: {novye_dostupnye}")

        rekursiya_perestanovok(
            dostupnye=novye_dostupnye,
            tekushiy_put=tekushiy_put,
            itogovye_perestanovki=itogovye_perestanovki,
            logger=logger,
            uroven=uroven + 1
        )
        
        udalenniy = tekushiy_put.pop()
        logger.append(f"{indent}<- Назад: Убираем '{udalenniy}'. Путь: {tekushiy_put}. (Возврат на уровень {uroven})")

    logger.append(f"{indent}--- Возврат (закончился цикл на уровне {uroven}) ---")

def generirovat_kombinatsii(elementy, logger):
    
    itogovye_kombinatsii = []
    elementy_list = list(elementy)
    
    logger.append("--- СТАРТ: Генерация КОМБИНАЦИЙ ---")
    logger.append(f"Входные элементы: {elementy_list}")

    rekursiya_kombinatsiy(
        elementy_list=elementy_list,
        start_index=0,
        tekushiy_put=[],
        itogovye_kombinatsii=itogovye_kombinatsii,
        logger=logger,
        uroven=0
    )
    
    logger.append("--- КОНЕЦ: Генерация КОМБИНАЦИЙ ---")
    return itogovye_kombinatsii

def rekursiya_kombinatsiy(elementy_list, start_index, tekushiy_put, itogovye_kombinatsii, logger, uroven):
    indent = "  " * uroven
    
    logger.append(f"{indent}--- Вызов (уровень {uroven}) ---")
    logger.append(f"{indent}Индекс элемента: {start_index}")
    logger.append(f"{indent}Частичный результат (текущий путь): {tekushiy_put}")

    if start_index == len(elementy_list):
        logger.append(f"{indent}!!! РЕЗУЛЬТАТ: {tekushiy_put} (Дошли до конца, добавляем в итог)")
        itogovye_kombinatsii.append(tekushiy_put.copy())
        logger.append(f"{indent}--- Возврат (базовый случай) ---")
        return
        
    
    element = elementy_list[start_index]
    
    logger.append(f"{indent}-> Шаг 1: НЕ ВЫБИРАЕМ '{element}'. Переходим к индексу {start_index + 1}.")
    rekursiya_kombinatsiy(
        elementy_list=elementy_list,
        start_index=start_index + 1,
        tekushiy_put=tekushiy_put,
        itogovye_kombinatsii=itogovye_kombinatsii,
        logger=logger,
        uroven=uroven + 1
    )
    
    logger.append(f"{indent}-> Шаг 2: ВЫБИРАЕМ '{element}'.")
    
    tekushiy_put.append(element)
    logger.append(f"{indent}    Частичный результат: {tekushiy_put}")

    rekursiya_kombinatsiy(
        elementy_list=elementy_list,
        start_index=start_index + 1,
        tekushiy_put=tekushiy_put,
        itogovye_kombinatsii=itogovye_kombinatsii,
        logger=logger,
        uroven=uroven + 1
    )
    
    udalenniy = tekushiy_put.pop()
    logger.append(f"{indent}<- Назад: Убираем '{udalenniy}'. Путь: {tekushiy_put}. (Возврат на уровень {uroven})")

    logger.append(f"{indent}--- Возврат (закончились оба шага для индекса {start_index}) ---")


if __name__ == "__main__":
    
    vhodnoy_nabor = {'A', 'B'} 

    print("=" * 60)
    print("        ЗАДАНИЕ 1: ПЕРЕСТАНОВКИ (Порядок важен)")
    print("=" * 60)
    
    log_perestanovok = []
    
    rezultat_p = generirovat_perestanovki(vhodnoy_nabor, log_perestanovok)
    
    print("\n--- 🏁 Итоговые ПЕРЕСТАНОВКИ: ---")
    pprint.pprint(rezultat_p)
    
    print("\n--- 📋 Полный ЛОГ вычислений (Перестановки): ---")
    for shag in log_perestanovok:
        print(shag)
        
        
    print("\n\n" + "=" * 60)
    print("        ЗАДАНИЕ 2: КОМБИНАЦИИ (Порядок НЕ важен)")
    print("=" * 60)
    
    log_kombinatsiy = []
    
    rezultat_k = generirovat_kombinatsii(vhodnoy_nabor, log_kombinatsiy)
    
    print("\n--- 🏁 Итоговые КОМБИНАЦИИ (Все подмножества): ---")
    pprint.pprint(rezultat_k)
    
    print("\n--- 📋 Полный ЛОГ вычислений (Комбинации): ---")
    for shag in log_kombinatsiy:
        print(shag)
