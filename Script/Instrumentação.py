#calculadora de range instrumentação

def cálculo_de_unidade(y_max, y_min, y, x_max, x_min):
    cálculo = (((y-y_min)/(y_max-y_min))*(x_max-x_min))+x_min
    print('%.3f' %cálculo)

print('Digite os dados seguindo o exemplo:\n'
      'Range Mínimo, Range Máximo, Valor Conhecido, Range Mínimo Desconhecido, Range Máximo Desconhecida')

entrada = input("Digite os valores:\n")
ymin, ymax, y, xmin, xmax = (float(x) for x in entrada.split(','))



cálculo_de_unidade(ymax,ymin,y,xmax,xmin)