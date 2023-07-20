def caudalOil(qmax, p_fluyente, p_reservorio):
    Q_oil = qmax*(1- (0.2*(p_fluyente/p_reservorio))-(0.8*((p_fluyente/p_reservorio)**2)))
    return Q_oil