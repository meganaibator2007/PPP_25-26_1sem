

if __name__ == "__main__":
    pass # Ваш код здесь
import pprint

# -----------------------------------------------------------------
#  Часть 1: Генерация всех ПЕРЕСТАНОВОК (Порядок важен)
# -----------------------------------------------------------------

def generirovat_perestanovki(elementy, logger):
    """
    Главная функция для генерации перестановок.
    Возвращает список всех перестановок и заполняет лог.
    
    :param elementy: Входной список или набор (set) элементов.
    :param logger: Внешняя коллекция (список) для логирования.
    :return: (list) Список всех перестановок.
    """
    
    itogovye_perestanovki = []
    # Конвертируем в список, чтобы было удобнее работать
    elementy_list = list(elementy) 
    
    logger.append("--- СТАРТ: Генерация ПЕРЕСТАНОВОК ---")
    logger.append(f"Входные элементы: {elementy_list}")
    
    # Запускаем рекурсивного помощника
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
    """
    Рекурсивная функция для поиска перестановок.
    Использует метод "выбрать и исключить".
    """
    indent = "  " * uroven # Отступ для наглядности лога
    
    logger.append(f"{indent}--- Вызов (уровень {uroven}) ---")
    logger.append(f"{indent}Доступные элементы: {dostupnye}")
    logger.append(f"{indent}Частичный результат (текущий путь): {tekushiy_put}")

    # --- Базовый случай рекурсии ---
    # Если доступных элементов не осталось, значит, мы собрали полную перестановку.
    if not dostupnye:
        logger.append(f"{indent}!!! РЕЗУЛЬТАТ: {tekushiy_put} (Добавляем в итог)")
        itogovye_perestanovki.append(tekushiy_put.copy()) # Важно: добавляем КОПИЮ
        logger.append(f"{indent}--- Возврат (базовый случай) ---")
        return

    # --- Рекурсивный шаг ---
    # Пробуем взять каждый из доступных элементов
    for i in range(len(dostupnye)):
        
        # 1. ВЫБОР: Берем элемент
        vybranniy = dostupnye[i]
        
        # 2. СОЗДАНИЕ НОВЫХ ДАННЫХ:
        # Новый список доступных (все, кроме того, что мы взяли)
        novye_dostupnye = dostupnye[:i] + dostupnye[i+1:]
        
        # Добавляем выбранный элемент в текущий путь
        tekushiy_put.append(vybranniy)
        
        logger.append(f"{indent}-> Шаг: Выбираем '{vybranniy}'. Путь: {tekushiy_put}. Остались: {novye_dostupnye}")

        # 3. РЕКУРСИВНЫЙ ВЫЗОВ:
        # Уходим вглубь с новыми данными
        rekursiya_perestanovok(
            dostupnye=novye_dostupnye,
            tekushiy_put=tekushiy_put,
            itogovye_perestanovki=itogovye_perestanovki,
            logger=logger,
            uroven=uroven + 1
        )
        
        # 4. "ШАГ НАЗАД" (Backtracking):
        # Мы вернулись из рекурсии. Убираем последний элемент из пути,
        # чтобы на следующей итерации цикла for попробовать другой элемент.
        udalenniy = tekushiy_put.pop()
        logger.append(f"{indent}<- Назад: Убираем '{udalenniy}'. Путь: {tekushiy_put}. (Возврат на уровень {uroven})")

    logger.append(f"{indent}--- Возврат (закончился цикл на уровне {uroven}) ---")

# -----------------------------------------------------------------
#  Часть 2: Генерация всех КОМБИНАЦИЙ (Порядок НЕ важен)
#  (Также известно как "Power Set" или "Все подмножества")
# -----------------------------------------------------------------

def generirovat_kombinatsii(elementy, logger):
    """
    Главная функция для генерации всех комбинаций (подмножеств).
    Возвращает список всех комбинаций и заполняет лог.
    
    :param elementy: Входной список или набор (set) элементов.
    :param logger: Внешняя коллекция (список) для логирования.
    :return: (list) Список всех комбинаций (подмножеств).
    """
    
    itogovye_kombinatsii = []
    elementy_list = list(elementy) # Нужны индексы
    
    logger.append("--- СТАРТ: Генерация КОМБИНАЦИЙ ---")
    logger.append(f"Входные элементы: {elementy_list}")

    # Запускаем рекурсивного помощника
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
    """
    Рекурсивная функция для поиска комбинаций.
    Использует метод "взять или не взять".
    """
    indent = "  " * uroven
    
    logger.append(f"{indent}--- Вызов (уровень {uroven}) ---")
    logger.append(f"{indent}Индекс элемента: {start_index}")
    logger.append(f"{indent}Частичный результат (текущий путь): {tekushiy_put}")

    # --- Базовый случай рекурсии ---
    # Мы дошли до конца списка. Текущий путь - это одна из комбинаций.
    if start_index == len(elementy_list):
        logger.append(f"{indent}!!! РЕЗУЛЬТАТ: {tekushiy_put} (Дошли до конца, добавляем в итог)")
        itogovye_kombinatsii.append(tekushiy_put.copy())
        logger.append(f"{indent}--- Возврат (базовый случай) ---")
        return
        
    # --- Рекурсивный шаг ---
    # У нас есть 2 варианта для элемента elementy_list[start_index]:
    
    element = elementy_list[start_index]
    
    # 1. "НЕ ВЗЯТЬ":
    # Мы пропускаем текущий элемент и переходим к следующему.
    logger.append(f"{indent}-> Шаг 1: НЕ ВЫБИРАЕМ '{element}'. Переходим к индексу {start_index + 1}.")
    rekursiya_kombinatsiy(
        elementy_list=elementy_list,
        start_index=start_index + 1,
        tekushiy_put=tekushiy_put,
        itogovye_kombinatsii=itogovye_kombinatsii,
        logger=logger,
        uroven=uroven + 1
    )
    
    # 2. "ВЗЯТЬ":
    # Мы берем текущий элемент, добавляем его в путь и переходим к следующему.
    logger.append(f"{indent}-> Шаг 2: ВЫБИРАЕМ '{element}'.")
    
    # Добавляем в путь
    tekushiy_put.append(element)
    logger.append(f"{indent}   Частичный результат: {tekushiy_put}")

    rekursiya_kombinatsiy(
        elementy_list=elementy_list,
        start_index=start_index + 1,
        tekushiy_put=tekushiy_put,
        itogovye_kombinatsii=itogovye_kombinatsii,
        logger=logger,
        uroven=uroven + 1
    )
    
    # "ШАГ НАЗАД" (Backtracking):
    # Мы вернулись из рекурсии "ВЗЯТЬ". Убираем элемент из пути,
    # чтобы не мешать ветке "НЕ ВЗЯТЬ", которая была выше.
    udalenniy = tekushiy_put.pop()
    logger.append(f"{indent}<- Назад: Убираем '{udalenniy}'. Путь: {tekushiy_put}. (Возврат на уровень {uroven})")

    logger.append(f"{indent}--- Возврат (закончились оба шага для индекса {start_index}) ---")


# -----------------------------------------------------------------
#  Пример использования
# -----------------------------------------------------------------
if __name__ == "__main__":
    
    # Для примера возьмем небольшой набор, чтобы лог был читаемым
    vhodnoy_nabor = {'A', 'B'} 
    # Вы можете поменять на {'A', 'B', 'C'}, но лог будет ОЧЕНЬ большим

    print("=" * 60)
    print("         ЗАДАНИЕ 1: ПЕРЕСТАНОВКИ (Порядок важен)")
    print("=" * 60)
    
    # Создаем внешнюю коллекцию для лога
    log_perestanovok = []
    
    # Запускаем функцию
    rezultat_p = generirovat_perestanovki(vhodnoy_nabor, log_perestanovok)
    
    print("\n--- 🏁 Итоговые ПЕРЕСТАНОВКИ: ---")
    pprint.pprint(rezultat_p)
    
    print("\n--- 📋 Полный ЛОГ вычислений (Перестановки): ---")
    for shag in log_perestanovok:
        print(shag)
        
        
    print("\n\n" + "=" * 60)
    print("         ЗАДАНИЕ 2: КОМБИНАЦИИ (Порядок НЕ важен)")
    print("=" * 60)
    
    # Создаем внешнюю коллекцию для лога
    log_kombinatsiy = []
    
    # Запускаем функцию
    rezultat_k = generirovat_kombinatsii(vhodnoy_nabor, log_kombinatsiy)
    
    print("\n--- 🏁 Итоговые КОМБИНАЦИИ (Все подмножества): ---")
    pprint.pprint(rezultat_k)
    
    print("\n--- 📋 Полный ЛОГ вычислений (Комбинации): ---")
    for shag in log_kombinatsiy:
        print(shag)
