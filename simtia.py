def gera_espaco(d, vetores):
    # Gera a matriz identidade
    identidade = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    
    # Verifica se cada vetor canônico está presente nos vetores fornecidos
    for vetor in identidade:
        if vetor not in vetores:
            return "Não"
    
    return "SimTia"

d, k = map(int, input().split())
vetores = [list(map(float, input().split())) for _ in range(k)]

print(gera_espaco(d, vetores), end='')