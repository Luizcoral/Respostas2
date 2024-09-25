import json

# Exemplo de dados de faturamento
faturamento_json = '''
{
    "faturamento": [0, 100, 200, 0, 300, 500, 0, 100, 150, 0, 700, 300, 0, 400, 350, 0]
}
'''

# Parse do JSON
faturamento_data = json.loads(faturamento_json)
faturamento = faturamento_data['faturamento']

def analisar_faturamento(faturamento):
    # Remover dias sem faturamento
    faturamento_validos = [x for x in faturamento if x > 0]

    # Cálculos
    menor_valor = min(faturamento_validos)
    maior_valor = max(faturamento_validos)
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)
    
    dias_acima_media = len([x for x in faturamento_validos if x > media_mensal])

    return menor_valor, maior_valor, dias_acima_media

menor, maior, dias_acima_media = analisar_faturamento(faturamento)
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Dias acima da média: {dias_acima_media}")
