def cadastrar_equipamento(id_equipamento, tipo, modelo):
    equipamento = {
        'id_equipamento': id_equipamento,
        'tipo': tipo,
        'modelo': modelo
    }
    equipamentos.append(equipamento)
