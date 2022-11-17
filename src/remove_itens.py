def define_obra(data):
    
    result = data.Descrição.str.contains("Manutenção|manutenção|Manutenções|manutenções|Automotiva|automotiva|MANUTENCAO|REFORMA|reformas", na=False)
    
    return (result.replace({True:'remove',False:'-'}))