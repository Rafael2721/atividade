# Simular quantidade de peso por item e por pessoa
# calcular valores
# apresentar relatório

qtdeCarvao = 1 # 1 pacote para cada 10 pessoas


qtdeCarneHomem = 0.4 # 400 gramas
qtdeFrangoHomem = 0.2 # 200 gramas
qtdeCervejaHomem = 4 #homem bebe 4 latas de cerveja
qtdeRefrigerenteHomem = 0.25 #500ml de refrigente

qtdeCarneMulher = 0.3
qtdeFrangoMulher = 0.1
qtdeCervejaMulher = 2
qtdeRefrigerenteMulher = 0.25 

qtdeCarneCrianca = 0.2 
qtdeFrangoCrianca = 0.1
qtdeCervejaCrianca = 0
qtdeRefrigerenteCrianca = 0.125


precoCarne = 50.0 # kg contra filé
precoFrango = 23.0 # kg de tulipa
precoCerveja = 3.99 #lata heineken 269ml
precoRefri = 8.0 # garrafa 2 litros
precoCarvao = 25.0 # pacote 4 kg



# Capturar as informações

print('Bem vindos a calculadora do seu churrasco')
print()
homens = float(input('Quantos homens vão no churrasco?: '))
mulheres = float(input('Quantas mulheres vão no churrasco?: '))
criancas = float(input('Quantas crianças vão no churrasco?: '))

#criar os calculos de peso:

carneHomem = homens * qtdeCarneHomem
carneMulher = mulheres * qtdeCarneMulher
carneCrianca = criancas * qtdeCarneCrianca

frangoHomem = homens * qtdeFrangoHomem
frangoMulher = mulheres * qtdeFrangoMulher
frangoCrianca = criancas * qtdeFrangoCrianca

cervejaHomem = homens * qtdeCervejaHomem
cervejaMulher = mulheres * qtdeCervejaMulher

refriHomem = homens * qtdeRefrigerenteHomem
refriMulher = mulheres * qtdeRefrigerenteMulher
refriCrianca = criancas * qtdeRefrigerenteCrianca

carvaoPacotes = (homens + mulheres + criancas) / 10

# Criar os calculos de gastos

valorCarneHomem = carneHomem * precoCarne
valorCarneMulher = carneMulher * precoCarne
valorCarneCrianca = carneCrianca * precoCarne

valorFrangoHomem = frangoHomem * precoFrango
valorFrangoMulher = frangoMulher * precoFrango
valorFrangoCrianca = frangoCrianca * precoFrango

valorRefriHomem = refriHomem * precoRefri
valorRefriMulher = refriMulher * precoRefri
valorRefriCrianca = refriCrianca * precoRefri

valorCarvao = carvaoPacotes * precoCarvao

valorCervejaHomem = cervejaHomem * precoCerveja
valorCervejaMulher = cervejaMulher * precoCerveja

total = valorCarneCrianca + valorCarneHomem + valorCarneMulher + valorFrangoCrianca + valorFrangoHomem + valorFrangoMulher + valorRefriCrianca + valorRefriHomem + valorRefriMulher + valorCervejaHomem + valorCervejaMulher + valorCarvao

# apresentar os resultados

print(f'Total de pessoas Homens: {homens}, Mulheres: {mulheres}, Crianças: {criancas}')   
print()
print(f'Total de {homens + mulheres + criancas} convidados.')
print()
print(f'Lista de Compras: {carneCrianca + carneHomem + carneMulher} kg de Carne.')
print(f'                  {frangoCrianca + frangoHomem + frangoMulher} kg de Frango.')
print(f'                  {refriCrianca + refriHomem + refriMulher} garrafas de refrigerante.')
print(f'                  {cervejaHomem + cervejaMulher} latas decerveja.')
print(f'                  {carvaoPacotes} pacotes de carvão.')
print()
print(f'Valor total da Compra: {total} reais.')
print(f'Valor por convidado: {total / (homens + mulheres + criancas)} reais.')
