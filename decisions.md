# Documentação de Decisões do Projeto

Este arquivo documenta as principais decisões técnicas tomadas durante o desenvolvimento do dashboard de monitoramento.

## 1. Por que a abordagem de regras para Análise de Sentimento?

Para este projeto, optei por uma abordagem de análise de sentimento baseada em regras (listas de palavras-chave) em vez de um modelo de Machine Learning (ML) pelos seguintes motivos:

* **Simplicidade e Rapidez de Implementação:** A criação de listas de palavras positivas e negativas é direta e não requer um ciclo complexo de treinamento, validação e deployment de um modelo. Para um case com escopo definido, essa abordagem é mais eficiente.
* **Interpretabilidade:** O resultado da análise é totalmente transparente. É fácil entender por que uma notícia foi classificada como "Positiva" ou "Negativa" – basta verificar quais palavras-chave do nosso dicionário ela contém. Modelos de ML, especialmente os mais complexos, podem funcionar como "caixas-pretas".
* **Custo Computacional Zero:** A análise de regras é extremamente leve e rápida, não exigindo GPUs ou consumo significativo de memória, o que é ideal para um dashboard simples em Streamlit.
* **Controle e Customização:** É muito fácil adicionar ou remover palavras das listas para ajustar a performance do classificador para o domínio específico ("Inteligência Artificial no Piauí"), sem a necessidade de re-treinamento.

Embora menos sofisticada, essa abordagem é perfeitamente adequada para o objetivo central do projeto: criar um painel simplificado para uma triagem inicial do tom das notícias.

## 2. Como lidar com erros ou falta de notícias no feed RSS?

A possibilidade de o feed RSS do Google Notícias não retornar nenhuma notícia para os termos de busca específicos ("Inteligência Artificial Piauí") foi tratada da seguinte forma:

* **Tratamento de Exceções na Coleta:** O script `coleta_dados.py` utiliza um bloco `try...except` para capturar `requests.exceptions.RequestException`. Caso ocorra um erro de conexão (ex: falha de DNS, HTTP 500), o erro é registrado no console e o script continua para o próximo termo de busca, evitando que a aplicação inteira falhe.
* **Verificação de DataFrame Vazio:** Após a coleta, tanto o módulo de processamento quanto a aplicação Streamlit (`app.py`) verificam se o DataFrame resultante está vazio (`if data.empty:`).
* **Feedback ao Usuário:** Se nenhum dado for retornado, o dashboard não tenta renderizar os gráficos ou a tabela. Em vez disso, exibe uma mensagem clara e amigável ao usuário, como: `"Nenhuma notícia foi encontrada nos feeds RSS para os termos de busca. Tente novamente mais tarde."`. Isso garante uma experiência de usuário robusta e informativa, mesmo na ausência de dados.