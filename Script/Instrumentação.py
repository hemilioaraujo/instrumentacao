#calculadora de range instrumentação

def cálculo_de_unidade(y_max, y_min, y, x_max, x_min):
    cálculo = (((y-y_min)/(y_max-y_min))*(x_max-x_min))+x_min
    print('%.3f' %cálculo)

print('Digite os dados seguindo o exemplo:\n'
      'Range Mínimo, Range Máximo, Valor Conhecido, Range Mínimo Desconhecido, Range Máximo Desconhecida')

entrada = input("Digite os valores:\n")
ymax, ymin, y, xmax, xmin = (float(x) for x in entrada.split(','))



cálculo_de_unidade(ymax,ymin,y,xmax,xmin)
#cálculo_por_sinal(0,4095,0,100,2136)
#cálculo_de_unidade(20,4,8,15,3)
#cálculo_de_sinal(20,4,15,3,8)
