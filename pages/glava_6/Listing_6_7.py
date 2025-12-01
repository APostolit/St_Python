# Листинг 6.7
def my_fun_1():
    print("Работает функция my_fun_1()")
    my_fun_2()

def my_fun_2():
    print("Работает функция my_fun_2()")

def main():
    print('Запущена функция main() - точка входа в программу')
    my_fun_1()

if __name__ == "__main__":
    main()
