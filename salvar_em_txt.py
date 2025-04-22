def salvar_em_txt():
    with open('colheitas.txt', 'w') as file:
        for colheita in colheitas:
            file.write(str(colheita) + '\n')

    with open('perdas.txt', 'w') as file:
        for perda in perdas:
            file.write(str(perda) + '\n')
