# Projeto de Modelo Preditivo de Crédito

Este projeto visa construir um modelo preditivo para avaliar o risco de concessão de crédito a clientes com base em dados demográficos e financeiros. O modelo é desenvolvido usando a linguagem Python e as bibliotecas populares de ciência de dados, como Pandas, NumPy, Matplotlib, Seaborn e Scikit-learn.

## Objetivo

O principal objetivo deste projeto é criar um modelo de aprendizado de máquina capaz de prever o score de crédito de um cliente com base em diversas características. Além disso, são realizadas análises exploratórias de dados e pré-processamento para garantir a qualidade dos dados de entrada no modelo.

## Tecnologias Utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Funcionalidades Principais

1. **Carregamento de Dados:**
   - Os dados são carregados a partir de um arquivo Excel (dados_credito.xlsx).

2. **Pré-processamento de Dados:**
   - Tratamento de valores nulos e outliers.
   - Conversão de tipos de dados, como a transformação da coluna 'ULTIMO_SALARIO' para valores numéricos.
   - Criação da coluna 'FAIXA_ETARIA' com base na idade.

3. **Visualização de Dados:**
   - Boxplots e histogramas são gerados para visualizar características numéricas.
   - Countplots são utilizados para visualizar variáveis categóricas.

4. **Codificação de Variáveis Categóricas:**
   - Utilização do LabelEncoder para codificar variáveis categóricas.

5. **Treinamento e Avaliação do Modelo:**
   - Utilização do modelo RandomForestRegressor do Scikit-learn.
   - Avaliação do desempenho do modelo usando validação cruzada e métrica R².
   - Exibição das importâncias das features.

6. **Previsão de Novos Dados:**
   - Um exemplo de previsão é fornecido para novos dados.

## Arquivos do Projeto

- **dados_credito.xlsx:** Arquivo contendo os dados de clientes.
- **modelo_random_forest.pkl:** Modelo treinado salvo.

## Licença

Este projeto é distribuído sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
