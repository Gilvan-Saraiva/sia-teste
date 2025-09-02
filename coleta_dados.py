import requests
import xml.etree.ElementTree as ET
import pandas as pd
from bs4 import BeautifulSoup

def fetch_news(search_terms=["Inteligência Artificial Piauí", "SIA Piauí"]):

    all_news = []
    for term in search_terms:
        url = f"https://news.google.com/rss/search?q={term.replace(' ', '+')}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
        try:
            response = requests.get(url)
            response.raise_for_status() 

            root = ET.fromstring(response.content)
            for item in root.findall('.//channel/item'):
                title = item.find('title').text
                link = item.find('link').text
                pub_date = item.find('pubDate').text
            
                description_html = item.find('description').text
                # Limpando o HTML da descrição
                soup = BeautifulSoup(description_html, 'html.parser')
                description_text = soup.get_text()

                all_news.append({
                    "titulo": title,
                    "link": link,
                    "descricao": description_text,
                    "data_publicacao": pub_date
                })
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar notícias para o termo '{term}': {e}")
            continue # Continua para o próximo termo de busca

    if not all_news:
        print("Nenhuma notícia encontrada.")
        return pd.DataFrame(columns=["titulo", "link", "descricao", "data_publicacao", "sentimento", "termos_chave"])

   
    df = pd.DataFrame(all_news).drop_duplicates(subset=['titulo']).head(15)
    return df

if __name__ == '__main__':
 
    noticias_df = fetch_news()
    print(f"Coletadas {len(noticias_df)} notícias.")
    print(noticias_df.head())