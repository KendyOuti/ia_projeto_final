import os
import cv2
import mediapipe as mp
import csv

CAMINHO_DATASET = r'C:\Projeto IA\train'

ARQUIVO_SAIDA = 'libras_dados.csv'

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)

with open(ARQUIVO_SAIDA, mode='w', newline='') as f:
    writer = csv.writer(f)
    colunas = ['label']
    for i in range(21):
        colunas.extend([f'x{i}', f'y{i}'])
    writer.writerow(colunas)

print(f"Iniciando processamento do dataset em: {CAMINHO_DATASET}")

total_imagens = 0
sucessos = 0

for letra_pasta in os.listdir(CAMINHO_DATASET):
    caminho_letra = os.path.join(CAMINHO_DATASET, letra_pasta)
    
    if os.path.isdir(caminho_letra):
        print(f"Processando letra: {letra_pasta}...")
        
        for nome_img in os.listdir(caminho_letra):
            if nome_img.lower().endswith(('.png', '.jpg', '.jpeg')):
                total_imagens += 1
                
                caminho_img = os.path.join(caminho_letra, nome_img)
                imagem = cv2.imread(caminho_img)
                
                if imagem is None:
                    continue

                imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
                
                results = hands.process(imagem_rgb)
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        coordenadas = []
                        for lm in hand_landmarks.landmark:
                            coordenadas.extend([lm.x, lm.y])
                        
                        with open(ARQUIVO_SAIDA, mode='a', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([letra_pasta] + coordenadas)
                        
                        sucessos += 1

print("-" * 30)
print("PROCESSAMENTO CONCLUÍDO!")
print(f"Total de imagens lidas: {total_imagens}")
print(f"Mãos detectadas e salvas: {sucessos}")
print(f"Dados salvos em: {ARQUIVO_SAIDA}")