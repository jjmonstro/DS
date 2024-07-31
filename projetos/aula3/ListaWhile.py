import os 
import math
os.system("cls")

enter = "s"
while enter == "s":
    print("""
Ex 1 Maior Valor
Ex 2 Pode Votar?
Ex 3 Senha Válida
Ex 4 Preço Maças
Ex 5 Ordem Crescente
Ex 6 Peso ideal
Ex 7 Poligono
Ex 8 Poligono ou não idetificado
Ex 9 Maior valor (sem ser igual)
Ex 10 Triangulo Equilatero, Isoscele ou Escaleno
Ex 11 Triangulo Retangulo, Acutangulo ou Obtsuangulo
Ex 12 Verifica numero primo """)
    opcao=int(input("Escolha um: "))
    print("\n")
    match opcao:
        case 1:
            os.system("cls")
            valor1 = float(input("Digite o valor 1: "))
            valor2 = float(input("Digite o valor 2: "))

            if valor1 > valor2:
                print(f"{valor1} é o maior")
            elif valor2 > valor1:
                print(f"{valor2} é o maior")
            else:
                print("Os valores devem ser diferentes")

        case 2:
            os.system("cls")
            idade = int(input("Digite seu ano de nascimento: "))

            if 2024 - idade >= 16:
                print("Pode votar Negão!!")
            else:
                print("Vai terminar o ensino fundamental")

        case 3:
            os.system("cls")

            senha = int(input("Digite a Senha: "))

            if senha == 1234:
                print("ACESSO PERMITIDO")
            else:
                print("ACESSO NEGADO") 

        case 4:
            os.system("cls")

            quantmaca = int(input("Quantas maças você comprou?"))

            if quantmaca < 12:
                valormaca = 0.30 
                valortotal = valormaca * quantmaca
                print(f"O valor total é isso {valortotal}")
            else:
                valormaca = 0.25
                valortotal = valormaca * quantmaca
                print(f"O valor total é isso {valortotal}")

        case 5:
                os.system("cls")    
                print("ESTÁ ERRADO com 6 7 5")
                valor1 = float(input("Digite o primeiro valor: "))
                valor2 = float(input("Digite o segundo valor: "))
                valor3 = float(input("Digite o terceiro valor: "))

                if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
                    print("Digite valores diferentes!")
                elif valor1 < valor2 and valor1 < valor3 and valor2 < valor3:
                    print(f"{valor1} {valor2} {valor3}")
                elif valor3 < valor2:
                    print(f"{valor1} {valor3} {valor2}")
                elif valor3 < valor1 and valor3 < valor2 and valor2 < valor1:
                    print(f"{valor3} {valor2} {valor1}")
                elif valor1 < valor2:
                    print(f"{valor3} {valor1} {valor2}")
                elif valor2 < valor1 and valor2 < valor3 and valor3 < valor1:
                    print(f"{valor2} {valor3} {valor1}")
                else:
                    print(f"{valor2} {valor1} {valor3}")

        case 6:
                os.system("cls")
                altura = float(input("Qual dua altura?\n"))
                sexo = int(input("""Qual seu sexo?
1:feminino
2:masculino\n"""))
                if sexo == 1:
                    pesoideal = (62.1 * altura)-44.7
                    print(f"Seu peso ideal é {pesoideal}")
                elif sexo == 2:
                    pesoideal = (72.7 * altura) - 58
                    print(f"Seu peso ideal é {pesoideal}")

        case 7:
                lados=int(input("Número de lados: "))
                medidaLados=float(input("Medida(cm) dos lados: "))

                if lados == 3:
                    area=(medidaLados*medidaLados)/2
                    print(f"TRIÂNGULO, área = {area}")
                elif lados==4:
                    area=medidaLados^2
                    print(f"QUADRADO, área = {area}")
                elif lados==5:
                    print("PENTÁGONO")
                else:
                    print("erro")

        case 8:
            lados=int(input("Número de lados: "))
            medidaLados=float(input("Medida(cm) dos lados: "))

            if lados < 3:
                print("Não é um Poligono!!")
            elif lados == 3:
                area=(medidaLados*medidaLados)/2
                print(f"TRIÂNGULO, área = {area}")
            elif lados==4:
                area=medidaLados^2
                print(f"QUADRADO, área = {area}")
            elif lados==5:
                print("PENTÁGONO")
            elif lados > 5:
                print("Poligono não idetificado!!")
            else:
                print("erro")


        case 9:
            os.system("cls")
             

            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            num3 = int(input("Digite o terceiro numero: "))

            if num1 > num2 and num1 > num3:
                print(f"O maior dos numeros é {num1}")
            if num2 > num1 and num2 > num3:
                print(f"O maior dos numeros é {num2}")
            if num3 > num1 and num3 > num2:
                print(f"O maior dos numeros é {num3}")

        case 10: 
            os.system("cls")
            
            lado1 = float(input("Fale a medida de um dos lados do triangulo: "))
            lado2 = float(input("Fale a medida do outro lado do triangulo: "))           
            lado3 = float(input("Fale a medida do terceiro lado do triangulo: "))

            if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
                print("Seu triangulo é Equilátero!")
            elif lado1 == lado2 or lado1 == lado3 or lado2  == lado3:
                print("Seu triangulo é Isóscele!")
            else:
                print("Seu triangulo é Escaleno!")

        case 11:
            os.system("cls")

            angulo1 = float(input("Digite o primeiro angulo de um triangulo: "))
            angulo2 = float(input("Digite o segundo angulo de um triangulo: "))
            angulo3 = float(input("Digite o terceiro angulo de um triangulo: "))

            if angulo1 == 90:
                print("Seu triangulo é Retangulo!")
            elif angulo1 > 90:
                print("Seu triangulo é Obsutangulo!")
            elif angulo1 < 90:
                print("Seu triangulo é Acutangulo!")

        case 12:
            os.system("cls")

            number = int(input("Digite um número: "))

            if number % 2 == 0 or number % 3 == 0 or number == 3 or number == 2:
                print("n primo")
            else:
                print("primo")

        case _:
            print("ERRO!! Opção invalida!!")
        
    enter = str(input("Deseja repetir? (s/n)"))

    
