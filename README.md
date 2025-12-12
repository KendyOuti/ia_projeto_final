# JCRINTC - PROJETO FINAL

Este guia rápido explica como configurar e executar o projeto em sua máquina.

## Pré-requisitos

Certifique-se de ter o [Python 3](https://www.python.org/downloads/) e o `git` instalados em seu sistema.

## Passo a Passo

Siga as etapas abaixo para clonar o repositório, instalar as dependências e executar o programa principal.

### 1. Clonar o Repositório

Abra o terminal ou prompt de comando e execute o seguinte para baixar o código-fonte:

```bash
git clone [https://github.com/KendyOuti/ia_projeto_final.git](https://github.com/KendyOuti/ia_projeto_final.git)
cd ia_projeto_final
````

### 2\. Instalar Dependências

Instale todas as bibliotecas Python necessárias listadas no arquivo `requirements.txt` usando o `pip`:

```bash
pip install -r requirements.txt
```

### 3\. Executar a Aplicação Principal

Inicie o programa principal (que irá utilizar o modelo de IA pré-treinado) com o seguinte comando:

```bash
python main.py
```

Siga as instruções apresentadas na tela para interagir com o sistema de reconhecimento.

-----

### (Opcional) Treinar o Modelo

Se você deseja retreinar o modelo de IA ou coletar novos dados, utilize os scripts auxiliares:

#### Coleta de Dados

Para coletar novos dados para treinamento (provavelmente usando a webcam):

```bash
python coleta.py
```

#### Treinamento

Para treinar o modelo utilizando os dados coletados:

```bash
python treinar.py
```

Executar a Aplicação Principal:

```bash
python main.py
```
