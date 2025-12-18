import json

if __name__ == "__main__":

class CurrencyConverter:
    base_currency = "RUB"
    rates = {}

    @classmethod
    def set_base(cls, currency):
        cls.base_currency = currency.upper()
        cls.rates[cls.base_currency] = 1.0

    @classmethod
    def add_rate(cls, currency, rate):
        cls.rates[currency.upper()] = float(rate)

    @classmethod
    def to_base(cls, amount, currency):
        currency = currency.upper()
        if currency not in cls.rates:
            raise ValueError(f"Неизвестная валюта: {currency}")
        return amount * cls.rates[currency]

class Money:
    def __init__(self, raw_input):
        self.raw_input = raw_input
        self.amount = 0.0
        self.currency = CurrencyConverter.base_currency
        self.parse(raw_input)

    def parse(self, text):
        raise NotImplementedError("Метод parse должен быть переопределен")

    @property
    def value_in_base(self):
        return CurrencyConverter.to_base(self.amount, self.currency)

    def __lt__(self, other):
        return self.value_in_base < other.value_in_base

    def __eq__(self, other):
        return self.value_in_base == other.value_in_base

    def __str__(self):
        base_val = self.value_in_base
        return (f"{self.amount:.2f} {self.currency} = "
                f"{base_val:.2f} {CurrencyConverter.base_currency}")

class MoneyCode(Money):
    def parse(self, text):
        parts = text.split()
        if len(parts) != 2:
            raise ValueError("Неверный формат code. Ожидается: СУММА ВАЛЮТА")
        self.amount = float(parts[0])
        self.currency = parts[1].upper()

class MoneyJson(Money):
    def parse(self, text):
        data = json.loads(text)
        self.amount = float(data["amount"])
        self.currency = data["currency"].upper()

class MoneyLocal(Money):
    SYMBOLS = {'₽': 'RUB', '$': 'USD', '€': 'EUR', '¥': 'CNY'}

    def parse(self, text):
        found_currency = None
        clean_text = text
        for symbol, code in self.SYMBOLS.items():
            if symbol in text:
                found_currency = code
                clean_text = text.replace(symbol, "")
                break
        
        if not found_currency:
             parts = text.split()
             if parts[-1].isalpha():
                 found_currency = parts.pop()
                 clean_text = "".join(parts)
             else:
                found_currency = CurrencyConverter.base_currency

        self.currency = found_currency
        clean_text = clean_text.replace(" ", "").replace(",", ".")
        self.amount = float(clean_text)

class MoneyDefault(Money):
    def parse(self, text):
        self.amount = float(text)
        self.currency = CurrencyConverter.base_currency

def create_money_object(line):
    if line.startswith("code "):
        return MoneyCode(line[5:])
    elif line.startswith("json "):
        return MoneyJson(line[5:])
    elif line.startswith("local "):
        return MoneyLocal(line[6:])
    elif line.startswith("default "):
        return MoneyDefault(line[8:])
    else:
        raise ValueError("Неизвестный формат строки")

def main():
    print("=== Система учета денежных сумм ===")
    
    base = input("Введите базовую валюту (например, RUB): ").strip()
    if not base: 
        print("Базовая валюта не введена. Используется RUB.")
        base = "RUB"
    CurrencyConverter.set_base(base)

    print(f"Базовая валюта установлена: {base}")
    print("Введите курсы валют (формат: USD 92.5). Пустая строка для завершения ввода курсов.")

    while True:
        line = input("> ").strip()
        if not line:
            break
        try:
            parts = line.split()
            if len(parts) == 2:
                CurrencyConverter.add_rate(parts[0], parts[1])
            else:
                print("Ошибка: формат строки должен быть 'ВАЛЮТА КУРС'")
        except ValueError:
            print("Ошибка: курс должен быть числом.")

    print("\nВведите суммы (формат: тип значение).")
    print("Типы: code, json, local, default.")
    print("Для выполнения операции введите команду: sum, max, min, list.")
    
    money_collection = []

    while True:
        line = input("Ввод/Команда > ").strip()
        if not line:
            continue

        if line.lower() in ['sum', 'max', 'min', 'list']:
            command = line.lower()
            
            if not money_collection:
                print("Список сумм пуст.")
                continue

            if command == 'list':
                print("\n--- Список всех сумм ---")
                for m in money_collection:
                    print(m)
            
            elif command == 'sum':
                total = sum(m.value_in_base for m in money_collection)
                print(f"\nTotal: {total:.2f} {CurrencyConverter.base_currency}")

            elif command == 'max':
                max_obj = max(money_collection)
                print(f"\nMax: {max_obj}")

            elif command == 'min':
                min_obj = min(money_collection)
                print(f"\nMin: {min_obj}")
            
            if input("\nЗавершить работу? (y/n): ").lower() == 'y':
                break
            else:
                print("Продолжайте ввод сумм или команд.")
                continue

        try:
            money_obj = create_money_object(line)
            money_collection.append(money_obj)
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
