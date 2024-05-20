def recomendar_plano(consumo):
    if consumo <= 10:
        return'Plano Essencial Fibra - 50Mpbs'
    if 10 < consumo <= 20:
        return'Plano Prata FIbra - 100Mpbs'
    if 20 < consumo:
        return'Plano Premium Fibra - 300Mpbs'

plano_recomendado = recomendar_plano(consumo)
    
consumo = float(input('Qual seu consumo medio de internet por mês: '))
print(plano_recomendado(consumo))

