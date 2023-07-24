def combustivel(tipo=str(), litro=float()):

    quantidade = float()
    gasoleo = float(litro * 135)
    gasolina = float(litro * 300)

    if tipo == 'A':
        if litro == 20:
            quantidade = float(gasoleo - gasoleo * (3/100))
        elif litro > 20:
            quantidade = float(gasoleo - gasoleo * (5/100))
        elif litro < 20:
            quantidade = gasoleo
    else:
        if tipo == 'G':
            if litro == 20:
                quantidade = float(gasolina - gasolina * (4/100))
            elif litro > 20:
                quantidade = float(gasolina - gasolina * (6/100))
            elif litro < 20:
                quantidade = gasolina

    return(quantidade)

tipos = str(input('Escolha o tipo de combustivel A-Gasoleo & G-Gasolina: '))
litros = float(input('Digite quantos litros vai querer: '))

resultado = float(combustivel(tipos, litros))

print('O valor a ser pago pelo cliente é: {:.2f}'.format(resultado))