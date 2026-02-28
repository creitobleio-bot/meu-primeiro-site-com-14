from random import randint

sorteado = randint(1, 10)

vidas = 3

while True:
    palpite = int(input('digite um numero de 0 a 10, qualquer um' \
    ': '))
    
    if palpite == sorteado:
        print('Boa! Voce acertou!!')
        break

    if palpite < sorteado:
        print('muito baixo, ze mane')
    elif palpite > sorteado:
        print('muito alto, ze mane')

    vidas = vidas - 1
    if vidas == 0:
        print('Ja era, vc perdeu!')
        break
