

if __name__ == "__main__":
    pass # Ваш код здесь
import random

def sozdat_pole(N, M):
    """
    Создает игровое поле (список списков) N x M
    и заполняет его случайными 0 или 1.
    """
    pole = []
    for _ in range(N):
        # Создаем одну строку (ряд)
        ryad = [random.randint(0, 1) for _ in range(M)]
        pole.append(ryad)
    return pole

def poschitat_stroki_i_stolbtsy(pole, N, M):
    """
    Подсчитывает, сколько строк и столбцов
    имеют сумму > 3.
    """
    # --- Считаем строки ---
    # sum(ryad) просто суммирует все элементы в списке
    kolichestvo_strok = 0
    for ryad in pole:
        if sum(ryad) > 3:
            kolichestvo_strok += 1

    # --- Считаем столбцы ---
    kolichestvo_stolbtsov = 0
    # Идем по каждому столбцу (индекс c)
    for c in range(M):
        summa_stolbtsa = 0
        # Идем по каждой строке (индекс r)
        for r in range(N):
            summa_stolbtsa += pole[r][c]
        
        if summa_stolbtsa > 3:
            kolichestvo_stolbtsov += 1
            
    return kolichestvo_strok, kolichestvo_stolbtsov

def naiti_ostrova(pole, N, M):
    """
    Находит размеры всех "островов" из 1.
    """
    # Создаем "карту" посещенных ячеек, чтобы не ходить дважды
    # Изначально она вся заполнена False (не посещено)
    posetili = [[False for _ in range(M)] for _ in range(N)]
    
    razmery_ostrovov = []

    def poisk_sosedey(r, c):
        """ Вспомогательная функция (рекурсивный поиск) """
        
        # --- Проверки, чтобы не выйти за пределы поля ---
        # 1. Если вышли за границы (вверх/вниз)
        if r < 0 or r >= N:
            return 0
        # 2. Если вышли за границы (влево/вправо)
        if c < 0 or c >= M:
            return 0
        # 3. Если это "вода" (0)
        if pole[r][c] == 0:
            return 0
        # 4. Если мы тут уже были
        if posetili[r][c]:
            return 0
        # ---
        
        # Если все проверки пройдены, значит, это часть острова
        
        # 1. Отмечаем, что мы тут были
        posetili[r][c] = True
        
        # 2. Текущий размер = 1 (эта ячейка)
        tekushiy_razmer = 1
        
        # 3. Проверяем всех 4-х соседей
        tekushiy_razmer += poisk_sosedey(r + 1, c) # Вниз
        tekushiy_razmer += poisk_sosedey(r - 1, c) # Вверх
        tekushiy_razmer += poisk_sosedey(r, c + 1) # Вправо
        tekushiy_razmer += poisk_sosedey(r, c - 1) # Влево
        
        return tekushiy_razmer

    # --- Главный цикл: проходим по каждой ячейке поля ---
    for r in range(N):
        for c in range(M):
            # Если это '1' и мы там еще не были — это новый остров
            if pole[r][c] == 1 and not posetili[r][c]:
                # Запускаем поиск соседей, чтобы найти весь остров
                razmer = poisk_sosedey(r, c)
                razmery_ostrovov.append(razmer)
                
    return razmery_ostrovov

def pechat_polya(pole):
    """Красиво печатает поле"""
    for ryad in pole:
        # ' '.join(...) превращает список [1, 0, 1] в строку "1 0 1"
        print(' '.join([str(kletka) for kletka in ryad]))


# --- Основная программа ---

# 1. Задаем размеры
N_STROK = 6
M_STOLBTSOV = 8

# 2. Генерируем поле
igrovoe_pole = sozdat_pole(N_STROK, M_STOLBTSOV)
print(f"--- 🎲 Игровое поле ({N_STROK}x{M_STOLBTSOV}) ---")
pechat_polya(igrovoe_pole)
print("-" * 30)

# 3. Считаем строки и столбцы
stroki, stolbtsy = poschitat_stroki_i_stolbtsy(igrovoe_pole, N_STROK, M_STOLBTSOV)
print(f"📊 Количество строк (где > 3 единиц): {stroki}")
print(f"📊 Количество столбцов (где > 3 единиц): {stolbtsy}")
print("-" * 30)

# 4. Ищем острова
razmery = naiti_ostrova(igrovoe_pole, N_STROK, M_STOLBTSOV)
print(f"🏝️  Найденные 'острова' и их размеры: {razmery}")
print(f"    Общее количество островов: {len(razmery)}")
