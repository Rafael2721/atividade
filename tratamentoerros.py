#errado
while True:
    try:
        
            n1= int(input('DIGITE UM NUMERO'))
            n2 = int(input("digite outro numero"))
            conta = n1/n2
        
    except ZeroDivisionError:
        print('não sei se vc aprendeu isso na escola, mas não e, dividir nada por 0 ')
    except ValueError:
        print('não da para dividir números por letras')
    else:
     print(f'{n1} dividido por {n2} é = {conta}')
     break
   

