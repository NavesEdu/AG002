#AG002:
# Ana Clara dos Santos Rosa
# Eduardo Naves Sant'Ana Azevedo

from training_measure import classifier
from inputs import x_input

print("AG002 - Recorrência do Câncer de Mama")

# se sair 1 não tem chance de ocorrência da doença, se sair 2 tem chance de recorrencia
if classifier.predict(x_input) == 1:
    print("Recorrencia apos o tratamento: Não")
if classifier.predict(x_input) == 2:
    print("Recorrencia apos o tratamento: Sim")
