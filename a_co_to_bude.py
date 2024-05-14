import random 


print("V téhle hře budete hádat délku náhodně vygenerovaného pole")

def náh_pole():
    low = 0
    high = 200
    cols = 1
    lrows = 2
    hrows = 15

    x = [random.choices(range(low,high), k=cols) for _ in range(lrows,hrows)]
    print("Jaká je délka tohohle pole?")
    print("----------------------------------------------------------------")
    print(', '.join(map(repr, x)))
    print("----------------------------------------------------------------")
    int(input("zadejte svou odpověď: "))

náh_pole()
