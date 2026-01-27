vendas = [
    {"mes": "Jan", "vendedor": "Ana", "valor": 150},
    {"mes": "Jan", "vendedor": "Ana", "valor": 100},
    {"mes": "Jan", "vendedor": "João", "valor": 200},
    {"mes": "Jan", "vendedor": "Maria", "valor": 80},

    {"mes": "Fev", "vendedor": "Ana", "valor": 300},
    {"mes": "Fev", "vendedor": "João", "valor": 150},
    {"mes": "Fev", "vendedor": "Maria", "valor": 220},
    {"mes": "Fev", "vendedor": "Pedro", "valor": 400},

    {"mes": "Mar", "vendedor": "Ana", "valor": 100},
    {"mes": "Mar", "vendedor": "João", "valor": 50},
    {"mes": "Mar", "vendedor": "Pedro", "valor": 200},
]

# 1) Total por vendedor
total_por_vendedor = {}

for venda in vendas:
    vendedor = venda["vendedor"]
    valor = venda["valor"]

    if vendedor not in total_por_vendedor:
        total_por_vendedor[vendedor] = 0

    total_por_vendedor[vendedor] += valor


# 2) Total por mês
total_por_mes = {}

for venda in vendas:
    mes = venda["mes"]
    valor = venda["valor"]

    if mes not in total_por_mes:
        total_por_mes[mes] = 0

    total_por_mes[mes] += valor


# 3) Contar vendedores com total > 500
vendedores_acima_500 = 0

for total in total_por_vendedor.values():
    if total > 500:
        vendedores_acima_500 += 1


# 4) Classificação dos vendedores
classificacao = {}

for vendedor, total in total_por_vendedor.items():
    if total <= 200:
        classificacao[vendedor] = "baixo"
    elif total <= 500:
        classificacao[vendedor] = "medio"
    else:
        classificacao[vendedor] = "alto"


print(total_por_vendedor)
print(total_por_mes)
print(vendedores_acima_500)
print(classificacao)








