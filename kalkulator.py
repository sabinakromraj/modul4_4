import logging

def calculator():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    
    print(">> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    operation = int(input())
    
    if operation < 1 or operation > 4:
        print("Niepoprawny numer operacji.")
        return
    
    num1 = float(input(f"Podaj składnik 1: "))
    num2 = float(input(f"Podaj składnik 2: "))
    
    if operation == 1:
        result = num1 + num2
        logging.info(f"Dodaję {num1} i {num2}")
    elif operation == 2:
        result = num1 - num2
        logging.info(f"Odejmuję {num2} od {num1}")
    elif operation == 3:
        result = num1 * num2
        logging.info(f"Mnożę {num1} i {num2}")
    elif operation == 4:
        if num2 == 0:
            print("Nie można dzielić przez 0.")
            return
        result = num1 / num2
        logging.info(f"Dzielę {num1} przez {num2}")
    
    print(f"Wynik to {result}")

if __name__ == "__main__":
    calculator()