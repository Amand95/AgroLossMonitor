def cadastrar_colheita(id_colheita, data, local, area_colhida, tipo_colheita):
    colheita = {
        'id_colheita': id_colheita,
        'data': data,
        'local': local,
        'area_colhida_ha': area_colhida,
        'tipo_colheita': tipo_colheita
    }
    colheitas.append(colheita)

