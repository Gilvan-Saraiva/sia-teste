import pandas as pd
import re
from collections import Counter

# Listas de palavras simples para análise de sentimento em português
PALAVRAS_POSITIVAS = [
    'avanço', 'crescimento', 'inova', 'inovação', 'melhora', 'desenvolvimento',
    'oportunidade', 'sucesso', 'positivo', 'benefício', 'fortalece', 'expansão',
    'otimiza', 'eficiência', 'solução'
]
PALAVRAS_NEGATIVAS = [
    'risco', 'ameaça', 'desafio', 'problema', 'preocupação', 'impacto negativo',
    'crise', 'dificuldade', 'barreira', 'ilegal', 'perigo', 'corte', 'redução'
]

def clean_text(text):
    """Remove caracteres especiais e converte para minúsculas."""
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.lower()

def analyze_sentiment_rule_based(text):
    """
    Classifica o sentimento de um texto com base em palavras-chave.

    Args:
        text (str): O texto a ser analisado.

    Returns:
        str: 'Positivo', 'Negativo' ou 'Neutro'.
    """
    text_limpo = clean_text(text)
    score = 0
    for word in PALAVRAS_POSITIVAS:
        if word in text_limpo:
            score += 1
    for word in PALAVRAS_NEGATIVAS:
        if word in text_limpo:
            score -= 1

    if score > 0:
        return 'Positivo'
    elif score < 0:
        return 'Negativo'
    else:
        return 'Neutro'

def extract_key_terms(text, num_terms=5):
    """Extrai os termos mais frequentes de um texto."""
    text_limpo = clean_text(text)
    # Palavras a serem ignoradas (stopwords)
    stopwords = set(['a', 'o', 'e', 'de', 'do', 'da', 'em', 'um', 'para', 'com', 'não', 'no', 'na'])
    words = [word for word in text_limpo.split() if word not in stopwords and len(word) > 3]
    most_common = Counter(words).most_common(num_terms)
    return ', '.join([word for word, count in most_common])

def process_data(df):
    """
    Aplica a limpeza, análise de sentimento e extração de termos a um DataFrame.
    """
    if df.empty:
        return df
        
    df['texto_completo'] = df['titulo'] + ' ' + df['descricao']
    df['sentimento'] = df['texto_completo'].apply(analyze_sentiment_rule_based)
    df['termos_chave'] = df['texto_completo'].apply(extract_key_terms)
    return df.drop(columns=['texto_completo'])

if __name__ == '__main__':
    # Exemplo de uso
    from coleta_dados import fetch_news
    noticias_df = fetch_news()
    if not noticias_df.empty:
        noticias_processadas_df = process_data(noticias_df.copy())
        print(noticias_processadas_df[['titulo', 'sentimento', 'termos_chave']].head())