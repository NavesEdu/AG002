print('Entre com os seus dados: ')

while True:
    a = int(input('Faixa etária: '))
    if(a>=1 and a<=9):
        break

while True:
    b = int(input('Pré ou pós-menopausa: '))
    if(1 <=b <=3):
        break

while True:
    c = int(input('Faixa do diâmetro do tumor: '))
    if(1 <=c <=12):
        break

while True:
    d = int(input('Número de linfonodos auxiliares: '))
    if(1 <=d <=13):
        break

while True:
    e = int(input('Penetração do tumor na cápsula do linfonodo: '))
    if(1 <=e <=2):
        break

while True:
    f = int(input('Gráu de malignidade do tumor: '))
    if(1 <=f <=3):
        break

while True:
    g = int(input('Mama em que o câncer pode ocorrer: '))
    if(1 <=g <=2):
        break

while True:
    h = int(input('Quadrante da mama afetado considerando o bico como o centro: '))
    if(1 <=h <=5):
        break

while True:
    i = int(input('Histórico de radioterapia: '))
    if(1 <=i <=2):
        break

x_input = [[a, b, c, d, e, f, g, h, i]]

# Recorrência após o tratamento: Não
# x_input = [[3,3,1,1,1,1,2,5,1]]

# Recorrência após o tratamento: Sim
# x_input = [[6,2,8,4,2,3,1,2,2]]
