def calcular_area_retangulo(comprimento,  largura):
    if comprimento < 0 or largura < 0:
        return 0
    else:
        area = comprimento * largura
        return area