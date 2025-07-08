# Letras de Músicas

Um aplicativo web simples feito com [Streamlit](https://streamlit.io/) que busca letras de músicas usando a API do Genius.

## Funcionalidades

- Busca letras de músicas por nome da banda e da música
- Exibe a letra encontrada diretamente na tela
- Interface simples e intuitiva

## Como usar

1. **Clone o repositório:**
   ```
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```
   python -m venv venv
   # No Windows:
   .\venv\Scripts\Activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```
   pip install -r requirements.txt
   ```

4. **Adicione seu token de acesso da Genius**  
   No arquivo `app.py`, substitua `"SEU_ACCESS_TOKEN"` pelo seu token pessoal da Genius.

5. **Coloque uma imagem chamada `banda.png` na pasta do projeto**  
   Ou altere o caminho da imagem no `app.py` para uma imagem de sua preferência.

6. **Execute o aplicativo:**
   ```
   streamlit run app.py
   ```

7. **Acesse no navegador:**  
   [http://localhost:8501](http://localhost:8501)

## Observações

- O app faz scraping da página da música no Genius para obter a letra, pois a API oficial não retorna a letra diretamente.
- Certifique-se de não compartilhar seu token de acesso da Genius publicamente.

## Licença

Este projeto é livre para uso educacional e pessoal.