import streamlit as st 
import Dados_str 

st.title("Filmes")


nome = st.text_input("Nome do filme: ")
ano = st.number_input("Ano do Filme:", min_value=2010, max_value=2024)
Nota = st.slider("Nota do filme:", min_value=0.0, max_value=10.0)

if st.button('Adicionar'):
    Dados_str.inserir_dados(nome, ano, Nota)
    st.success("Filme adicionado com sucesso!")
    
filmes = Dados_str.obter_dados()
st.header("Lista de Filmes")
st.table(filmes)