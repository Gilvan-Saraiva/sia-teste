


# Dashboard de Monitoramento: IA no Piauí

Este projeto implementa um dashboard simplificado para monitorar menções sobre "Inteligência Artificial no Piauí" em fontes de notícias públicas.

## Funcionalidades

- **Coleta de Dados:** Busca notícias em tempo real do feed RSS do Google Notícias.
- **Análise de Sentimento:** Classifica cada notícia como Positiva, Negativa ou Neutra usando uma abordagem baseada em regras.
- **Visualização de Dados:**
  - Gráfico de pizza com a distribuição dos sentimentos.
  - Nuvem de palavras com os termos mais frequentes.
  - Tabela interativa com os detalhes das notícias.

## Setup e Execução

1.  **Clone o repositório:**
    ```bash
    git clone [git@github.com:Gilvan-Saraiva/sia-teste.git](git@github.com:Gilvan-Saraiva/sia-teste.git)
    cd sia-teste
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    ou
    .venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run app.py
    ```

## Estrutura do Projeto

- `app.py`: Script principal do Streamlit.
- `coleta_dados.py`: Módulo responsável pela coleta de notícias.
- `processamento.py`: Módulo para limpeza e análise de sentimento.
- `requirements.txt`: Lista de dependências Python.
- `DECISIONS.md`: Documentação das decisões de projeto.

## Transparência

    Cerca de 90% do README.md foi feito com ia
