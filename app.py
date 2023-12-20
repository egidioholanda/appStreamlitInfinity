import streamlit as st

st.title('Exemplo de Imagem no Streamlit')
radio_selecionado = st.radio('Selecione a variedade',["Setosa","Versicolor",'Virginica'],horizontal=True)
if radio_selecionado == 'Setosa':
   imagem = 'setosa.png'
elif radio_selecionado == 'Versicolor':
   imagem = 'versicolor.png'
else:
   imagem = 'virginica.png'
   
st.image(imagem, width=300)




