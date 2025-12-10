import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# 1. Carregar os dados
try:
    dados = pd.read_csv('libras_dados.csv')
except FileNotFoundError:
    print("Erro: O arquivo 'libras_dados.csv' não foi encontrado. Rode o script de processamento antes.")
    exit()


dados.dropna(inplace=True)

# Separa as coordenadas (X) da letra (y)
X = dados.drop('label', axis=1)
y = dados['label']


# Isso garante que se você tem 100 fotos de 'A' e 100 de 'B',
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Criar e treinar o modelo

model = RandomForestClassifier(n_estimators=100, n_jobs=-1) 
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acuracia * 100:.2f}%")


print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))


with open('modelo_libras.p', 'wb') as f:
    pickle.dump(model, f)
    
print("Modelo salvo com sucesso como 'modelo_libras.p'")