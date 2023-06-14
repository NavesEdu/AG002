from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import hamming_loss
from connection import frame

feature_cols = ['age', 'menopause', 'tumor-size',
                'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat']
x = frame.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9]].values
y = frame.iloc[:, 10].values

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0
)

classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)

print('\n---------------------------------------[INICIO DAS METRICAS]--------------------------------------')
#Medindo a acurácia do modelo com base nas métricas de avaliação
y_predict = classifier.predict(x_test)

print('\nAcuracy:', metrics.accuracy_score(y_test, y_predict)*100,'%') #mostra a porcentagem de acerto
print('Acuracy:', metrics.accuracy_score(y_test, y_predict, normalize=False),'\n') #mostra quantas acertou

print(classification_report(y_test, y_predict)) #mostra as metricas principais da classificacao

concordancia = cohen_kappa_score(y_test, y_predict)
print('Coeficiente Kappa de Cohen (Concordancia):', concordancia)
if 0 <= concordancia <= 0.2:
    print('Concordancia minima')
if 0.21 <= concordancia <= 0.4:
    print('Concordancia razoavel')
if 0.41 <= concordancia <= 0.6:
    print('Concordancia moderada')
if 0.61 <= concordancia <= 0.8:
    print('Concordancia substancial')
if 0.81 <= concordancia <= 1:
    print('Concordancia perfeita')

print('\nPercentual de Labels previstas incorretamente:', hamming_loss(y_test, y_predict)*100,'%')

print('\nMedia Harmonica Ponderada entre precisao e recall:', metrics.fbeta_score(y_test, y_predict, beta=0.5))
#valor ideal em 1 e seu pior valor em 0

print('\n---------------------------------------[FIM DAS METRICAS]--------------------------------------')