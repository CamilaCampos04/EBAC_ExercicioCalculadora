num1 = 0 ; num2 = 0

# Parte que vai receber os valores:
print('Olá! Seja bem vinda a calculadora!')
print('Para começar digite os dois númeroa que deseja calcular.')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

#Confirmação dos valores
print('Os números que você digitou foram: ', num1, ' e ', num2)

#Realização da conta
print('As opções de operações são: soma, menos, vezes e dividir')
calc = input('Escreva qual deseja realizar: ')

print('Você selecionou', calc)

#Realização do calculo
if (calc == 'soma'):
	print('A soma é: ', num1 + num2)

elif (calc == 'menos'):
        print('A subtração é: ', num1 - num2)

elif (calc == 'vezes'):
        print('A muliplicação é: ', num1 * num2)

elif (calc == 'dividir'):
        print('A divisão é: ', num1 / num2)

else:
	print('Você não selecionou uma opção valida. Execute o programa e tente novamente.')
