def tower_builder(n_floors, symbol):
    length=2*(n_floors-1)+1   #length of the lowest floor of tower
    result=[]
    for i in range (n_floors):
        result.append((symbol*(i*2+1)).center(length))
    return result

def output_tower(tower):
    for el in tower:
        print(el)

def main():
    while True:
        try:    
            num=int(input("Введите количество этажей башни: "))
        except Exception as e:
            print("Введены некоректные данные: ",e)
            continue
        smb=input("Введите символ, из которого хотите построить башню: ")[0]
        print("Башня:")
        output_tower(tower_builder(num,smb))
        answ=input("Вы хотите продолжить? 1 - да, что-угодно - нет: ")
        if answ.lower() != "1":
            break    

if __name__=="__main__":
    main()