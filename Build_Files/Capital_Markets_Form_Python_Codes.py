print('')
print('Formulário de Mercado de Capitais')
print('')
print('vp: Valor Presente')
print('VF: Valor Futuro')
print('TJ: Taxa de Juros')
print('TI: Tempo do Investimento')
print('')
print('Escolha o resultado que deseja obter')
print('')

while True:
    z = str(input('(vp),(VF),(TJ),(TI): '))
    print('')
    if 'vp' == z:
        print('Para calcular utilizando na fórmula (VF, TI e TJ): A')
        print('')
        n = str(input('(A): '))
        print('')
        if 'A' == n:
            def vp():
                VF = float(input("Adicionar o valor de VF: "))
                TI = float(input("Adicionar o valor de TI: "))
                TJ = float(input("Adicionar o valor de TJ em %: "))
                vp1 = (VF / ((1 + (TJ / 100)) ** TI))
                return "vp:{}".format(vp1)
            print('')
            print(vp())
            print('')
    if 'VF' == z:
        print('Para calcular utilizando na fórmula (VP, TI e TJ): A')
        print('')
        n = str(input('(A): '))
        print('')
        if 'A' == n:
            def VF():
                vp = float(input("Adicionar o valor de vp: "))
                TI = float(input("Adicionar o valor de TI: "))
                TJ = float(input("Adicionar o valor de TJ em %: "))
                VF1 = (vp * ((1 + (TJ / 100)) ** TI))
                return "VF:{}".format(VF1)
            print('')
            print(VF())
            print('')
    if 'TJ' == z:
        print('Para calcular utilizando na fórmula (VF, vp e TI): A')
        print('')
        n = str(input('(A): '))
        print('')
        if 'A' == n:
            def TJ():
                VF = float(input("Adicionar o valor de VF: "))
                vp = float(input("Adicionar o valor de vp: "))
                TI = float(input("Adicionar o valor de TI: "))
                TJ1 = ((VF/vp)**(1/TI))-1
                return "TJ:{}%".format(TJ1 * 100)
            print('')
            print(TJ())
            print('')
    if 'TI' == z:
        print('Para calcular utilizando na fórmula (VF, vp e TJ): A')
        print('')
        n = str(input('(A): '))
        print('')
        if 'A' == n:
            def TI():
                import math
                VF = float(input("Adicionar o valor de VF: "))
                vp = float(input("Adicionar o valor de vp: "))
                TJ = float(input("Adicionar o valor de TJ em %: "))
                TI1 = math.log((VF / vp), (TJ / 100) + 1)
                return "TI:{}".format(TI1)
            print('')
            print(TI())
            print('')