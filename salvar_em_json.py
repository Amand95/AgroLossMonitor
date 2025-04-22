import json

def salvar_em_json():
    with open('colheitas.json', 'w') as file:
        json.dump(colheitas, file, indent=4)

    with open('perdas.json', 'w') as file:
        json.dump(perdas, file, indent=4)
