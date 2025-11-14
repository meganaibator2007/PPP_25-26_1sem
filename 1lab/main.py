import random


if __name__ == "__main__":
    def sozdat_pole(N, M):
        pole = []
        for _ in range(N):
            ryad = [random.randint(0, 1) for _ in range(M)]
            pole.append(ryad)
        return pole
    
    def poschitat_stroki_i_stolbtsy(pole, N, M):
        kolichestvo_strok = 0
        for ryad in pole:
            if sum(ryad) > 3:
                kolichestvo_strok += 1
    
        kolichestvo_stolbtsov = 0
        for c in range(M):
            summa_stolbtsa = 0
            for r in range(N):
                summa_stolbtsa += pole[r][c]
            
            if summa_stolbtsa > 3:
                kolichestvo_stolbtsov += 1
                
        return kolichestvo_strok, kolichestvo_stolbtsov
    
    def naiti_ostrova(pole, N, M):
        posetili = [[False for _ in range(M)] for _ in range(N)]
        
        razmery_ostrovov = []
    
        def poisk_sosedey(r, c):
            
            if r < 0 or r >= N:
                return 0
            if c < 0 or c >= M:
                return 0
            if pole[r][c] == 0:
                return 0
            if posetili[r][c]:
                return 0
            
            posetili[r][c] = True
            
            tekushiy_razmer = 1
            
            tekushiy_razmer += poisk_sosedey(r + 1, c)
            tekushiy_razmer += poisk_sosedey(r - 1, c)
            tekushiy_razmer += poisk_sosedey(r, c + 1)
            tekushiy_razmer += poisk_sosedey(r, c - 1)
            
            return tekushiy_razmer
    
        for r in range(N):
            for c in range(M):
                if pole[r][c] == 1 and not posetili[r][c]:
                    razmer = poisk_sosedey(r, c)
                    razmery_ostrovov.append(razmer)
                    
        return razmery_ostrovov
    
    def pechat_polya(pole):
        for ryad in pole:
            print(' '.join([str(kletka) for kletka in ryad]))
    
    
    N_STROK = 6
    M_STOLBTSOV = 8
    
    igrovoe_pole = sozdat_pole(N_STROK, M_STOLBTSOV)
    print(f"--- 🎲 Игровое поле ({N_STROK}x{M_STOLBTSOV}) ---")
    pechat_polya(igrovoe_pole)
    print("-" * 30)
    
    stroki, stolbtsy = poschitat_stroki_i_stolbtsy(igrovoe_pole, N_STROK, M_STOLBTSOV)
    print(f"📊 Количество строк (где > 3 единиц): {stroki}")
    print(f"📊 Количество столбцов (где > 3 единиц): {stolbtsy}")
    print("-" * 30)
    
    razmery = naiti_ostrova(igrovoe_pole, N_STROK, M_STOLBTSOV)
    print(f"🏝️  Найденные 'острова' и их размеры: {razmery}")
    print(f"    Общее количество островов: {len(razmery)}")
