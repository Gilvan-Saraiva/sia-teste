import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px


from coleta_dados import fetch_news
from processamento import process_data

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Menções | IA no Piauí",
    page_icon="🤖",
    layout="wide"
)

# Funções de Cache
@st.cache_data(ttl=3600) # Cache de 1 hora
def load_and_process_data():
    """Carrega e processa os dados, usando cache para evitar múltiplas buscas."""
    raw_data = fetch_news()
    if raw_data.empty:
        return pd.DataFrame()
    processed_data = process_data(raw_data)
    return processed_data

# Título e Descrição 
st.title("🤖 Monitor de Menções sobre Inteligência Artificial no Piauí")
st.markdown("""
Este painel monitora notícias públicas sobre o tema "Inteligência Artificial no Piauí",
analisando o sentimento e os termos mais recorrentes.
""")

# --- Carregar Dados ---
data = load_and_process_data()

if data.empty:
    st.warning("Nenhuma notícia foi encontrada nos feeds RSS para os termos de busca. Tente novamente mais tarde.")
else:
    # --- Layout do Dashboard ---
    col1, col2 = st.columns((1, 1.5))

    with col1:
        # Gráfico de Pizza (Sentimentos)
        st.subheader("Distribuição de Sentimentos")
        sentiment_counts = data['sentimento'].value_counts()
        fig_pie = px.pie(
            sentiment_counts,
            values=sentiment_counts.values,
            names=sentiment_counts.index,
            color=sentiment_counts.index,
            color_discrete_map={
                'Positivo': '#4CAF50',
                'Negativo': '#F44336',
                'Neutro': '#607D8B'
            }
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        # Nuvem de Palavras
        st.subheader("Termos Mais Frequentes")
        all_text = ' '.join(data['titulo'])
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='viridis'
        ).generate(all_text)

        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

    # --- Tabela Interativa ---
    st.subheader("Notícias Coletadas")
    st.dataframe(data[['titulo', 'sentimento', 'termos_chave', 'link']])

# --- Rodapé ---
st.markdown("---")
st.markdown("""
<small>**Aviso sobre Limitações:** Esta análise de sentimento é baseada em regras simples (palavras-chave)
e pode não capturar sarcasmo, ironia ou contextos complexos. É uma ferramenta de triagem inicial
e não deve ser usada para conclusões definitivas.</small>
""", unsafe_allow_html=True)
st.markdown("""
<small>**Uso de IA:** Partes deste código, como a estrutura inicial do Streamlit e as funções de
visualização, foram desenvolvidas com o auxílio de um modelo de linguagem (IA) para acelerar
o desenvolvimento e garantir as melhores práticas.</small>
""", unsafe_allow_html=True)