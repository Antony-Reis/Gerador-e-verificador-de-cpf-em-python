def validar_cpf(cpf, retorna_bool=False):

    cpf_format = cpf.replace('.','').replace('-','')

    if not cpf_format.isdecimal or len(cpf_format) != 11:
        if retorna_bool:
             return False
        else:
            return f'CPF {cpf} inválido'

    else:
        cpf9 = cpf_format[:9]
         #calcular primeiro digito
        cpf_soma1 = 0
        for i,n in enumerate(cpf9):
            cpf_soma1 += int(n) * (10-i)
            
        cpf_soma1 *= 10

        resto_cpf1 = cpf_soma1 % 11

        if resto_cpf1 > 9:
                primeiro_digito = 0 
        else:
                primeiro_digito = resto_cpf1

         #calcular o segundo digito

        cpf10 = cpf_format[:9] + str(primeiro_digito)
        cpf_soma2 = 0

        for i,n in enumerate(cpf10):
            cpf_soma2 += int(n) * (11-i)

            
        cpf_soma2 *= 10

        resto_cpf2 = cpf_soma2 % 11

        if resto_cpf2 > 9:
                segundo_digito = 0 
        else:
            segundo_digito = resto_cpf2

        dois_ultimos = str(primeiro_digito) + str(segundo_digito)
            
        if cpf_format[-2:] == dois_ultimos:
            if retorna_bool:
             return True
            else:
                return f'CPF {cpf} válido!'
        else:
            if retorna_bool:
             return False
            else:
                return f'CPF {cpf} inválido!'
   
from random import randint   

while True:
    control = input('1 para validar um cpf\n2 para gerar um cpf\n3 para sair\n').strip()

    if control == '3':
        print('Programa encerrado')
        break

    elif control == '1':
        cpf_user = input('Insira um cpf para validação: ').strip()
        print(validar_cpf(cpf_user))

        
    elif control == '2':
        try:
            qntd_cpf = int(input('Insira quantos cpfs deseja gerar: \n'))
            cpfs = []
            for i in range(qntd_cpf):

                cpf_valido = False

                while not cpf_valido:
                    cpf_criado = "".join([str(randint(0, 9)) for i in range(11)])
                    cpf_valido = True if validar_cpf(cpf_criado, retorna_bool=True) else cpf_valido
                cpfs.append(cpf_criado)

            print(*cpfs, sep='\n')
                
        except ValueError:
            print('ERRO, insira um valor inteiro!')

    else:
        print('Comando inválido!')
            