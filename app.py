import streamlit as st
import requests
import pandas as pd

# Config inicial

st.set_page_config(page_title="FilmesFlix", layout="centered")

API_URL = "http://127.0.0.1:8000/" # ENdereço FASTAPI

st.title("FilmesFlix")
st.caption("Baseado no modelo SVD - Streamlit Interface")

# Entrada do usuário
st.sidebar.header("Configurações")
user_id = st.sidebar.number_input("ID do usuário", min_value=1, step=1, value=10)
n_recs = st.sidebar.slider("Quantidade de recomendações:", 1, 10, 5)

# Botão para recomendar
if st.sidebar.button("Me recomende"):
    with st.spinner("Buscando recomendações de filmes personalizadas"):
        try:
            response = requests.get(f"{API_URL}/recommend/{user_id}?n={n_recs}")
            if response.status_code == 200:
                data = response.json()

                if "error" in data:
                    st.error(data["error"])

                else:
                    recs = pd.DataFrame(data["recommendations"])
                    st.success(f"Top {n_recs} recomendações para o usuário {user_id}:")
                    st.dataframe(recs[['title', 'predicted_rating']].rename(
                        columns={'title': 'Filme', 'predicted_rating': 'Nota Prevista'}
                    ))


                    # Visual mais bonito com cartões
                    for _, row in recs.iterrows():
                        st.markdown(f"""
                        🎬 **{row['title']}**  
                        ⭐ *Nota prevista:* `{row['predicted_rating']}`  
                        ---
                        """)
            else:
                st.error("Erro ao conectar à API. Verifique se ela está rodando.") 
        except Exception as e:
            st.error(f"erro: {e}")

else:
    st.info("Escolha um usuário e clique em 'Me recomende' para começar.")


# Rodapé
st.markdown("----")
st.caption("Desenvolvido com Python + FastAPI + Streamlit + Surprise")