"""
Gera X CPFs
"""

vezes = int(input('Quantos CPFs você deseja gerar? '))
while vezes > 0:

    import random

    cpf = [random.randint(0, 9) for p in range(0, 9)]
    cpf_str = list(map(str, cpf))
    cpf_str_join = ''.join(cpf_str)

    cpf_int = []

    #  Transforma a string em int dentro da lista cpf_int
    for x in cpf:
        #  print(x)
        cpf_int.append(int(x))

    #  print(cpf_int)

    #  Primeiro cálculo
    calculo_1 = 10
    res_mult_1 = []

    for n1 in cpf_int:
        if calculo_1 >= 2:
            n1 = n1 * calculo_1
            calculo_1 -= 1
            res_mult_1.append(n1)

    #  print(sum(res_mult_1))
    sum_res_mult_1 = sum(res_mult_1)
    divsao_1 = 11 - (sum_res_mult_1 % 11)

    if divsao_1 > 9:
        prim_dig = 0
    else:
        prim_dig = divsao_1

    tamanho = len(cpf_int)
    cpf_int.insert(tamanho, prim_dig)
    #  print(cpf_int)

    #  Primeiro cálculo
    calculo_2 = 11
    res_mult_2 = []

    for n2 in cpf_int:
        if calculo_2 >= 2:
            n2 = n2 * calculo_2
            calculo_2 -= 1
            res_mult_2.append(n2)

    #  print(sum(res_mult_2))
    sum_res_mult_2 = sum(res_mult_2)
    divsao_2 = 11 - (sum_res_mult_2 % 11)

    if divsao_2 > 9:
        seg_dig = 0
    else:
        seg_dig = divsao_2

    tamanho = len(cpf_int)

    cpf_int.insert(tamanho, seg_dig)
    #  print(cpf_int)

    print(f'CPF para cadastrar como mesário: {cpf_str_join}-{prim_dig}{seg_dig}')

    vezes -= 1
