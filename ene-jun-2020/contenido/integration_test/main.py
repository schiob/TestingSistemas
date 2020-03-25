

def CalcCaloriasPlatillo(platillo):
    total_cal = 0

    for ing in platillo.ingredientes:
        total_cal += ing["ingrediente"].KalXUnidad * ing["cantidad"]
    return total_cal

def CalcCaloriasComida(comida):
    total_cal = 0
    # Recorrer platillos
    for plat in comida.platillos:
        # Por cada platillo calcular las calorias del platillo
        cal_platillo = CalcCaloriasPlatillo(plat)
        total_cal += cal_platillo
        
    return total_cal

def SePuedeComer(dieta, comida):
    # Cuanto llevo
    llevo = dieta.calcularCuantoLleva()

    # Calcular lo de la comida
    cal_comida = CalcCaloriasComida(comida)

    # Hacer el cálculo para ver si entra o no comparando con max calorias de la dieta
    if llevo + cal_comida > dieta.max_calorias:
        return False
    return True