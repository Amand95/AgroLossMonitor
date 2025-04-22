import uuid

colheitas = []

def cadastrar_colheita(data, estado, tipo_colheita):
    id_colheita = str(uuid.uuid4())  # Gera um ID único automaticamente
    colheita = {
        'id_colheita': id_colheita,
        'data': data,
        'estado': estado,
        'tipo_colheita': tipo_colheita
    }
    colheitas.append(colheita)
