def define_obra(data):
    
    result = data.Descrição.str.contains("Manutenção|manutenção|Manutenções|manutenções|Automotiva|AUTOMOTIVO|AUTOMOTIVA|MANUTENÇÃO|automotiva|MANUTENCAO|REFORMA|reformas", na=False)
    
    return (result.replace({True:'remove',False:'-'}))

def remove_from_objeto(data):
    
    result = data.Objeto.str.contains("Manutenção|manutenção|Manutenções|manutenções|Automotiva|AUTOMOTIVO|AUTOMOTIVA|MANUTENÇÃO|automotiva|MANUTENCAO|REFORMA|reformas", na=False)
    
    return (result.replace({True:'remove',False:'-'}))