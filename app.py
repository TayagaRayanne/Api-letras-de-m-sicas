import requests
import streamlit as st
from bs4 import BeautifulSoup

# Função para buscar a letra da música
def buscar_letra(banda, musica):
    access_token = "dPuGlgSV5UG_u8rZdMAFfBZq0V9q5CSYe6VBprED6sWTNPugVZx34SsPceJPINpO"  # Substitua pelo seu token da Genius
    headers = {"Authorization": f"Bearer {access_token}"}
    query = f"{banda} {musica}"  # Monta a consulta de busca
    endpoint = f"https://api.genius.com/search?q={query}"
    
    # Faz a requisição para a API do Genius
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        return ""  # Retorna vazio se houver erro na requisição
    
    # Pega os resultados da busca
    hits = response.json()["response"]["hits"]
    if not hits:
        return ""  # Retorna vazio se não encontrar resultados
    
    # Pega a URL da primeira música encontrada
    song_url = hits[0]["result"]["url"]
    
    # Faz scraping da página da música para pegar a letra
    page = requests.get(song_url)
    soup = BeautifulSoup(page.text, "html.parser")
    lyrics = ""
    # Procura os blocos de texto da letra
    for div in soup.find_all("div", attrs={"data-lyrics-container": "true"}):
        lyrics += div.get_text(separator="\n")
    return lyrics.strip()  # Retorna a letra limpa

# Exibe uma imagem no topo do app (pode ser local ou da internet)
st.image("C:/Users/tayga/Downloads/banda.jpeg", width=300)

# Título do app
st.title("Letras de Músicas")

# Campos de entrada para banda e música
banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")

# Quando o botão é pressionado, busca e exibe a letra
if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Encontramos a letra da música!")
        st.text(letra)
    else:
        st.error("Letra não encontrada! Tente outra música ou banda.")