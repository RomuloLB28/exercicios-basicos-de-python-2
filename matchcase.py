#fazer um programa usando matchcase

dia = int(input("Digite 1 para domingo, 2 para segunda feira, 3....\n"))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("sexta")
    case 7:
        print("sábado")
    case _:
        print("Dia invalido")
    
