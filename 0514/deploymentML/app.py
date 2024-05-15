import pickle
#Abrir  o arquivo do modelo treinado
with open('model/svc_model.pkl', 'rb') as f:
    model = pickle.load(f)

#Método para predição
def predict(data, model=model):
    return model.predict(data)

#print(predict([[2.5, 3.4, 2.4,3.3]]))
## ********* WEB APP ************
import streamlit as st
st.title('Classificador de Flores de Iris')
st.markdown('App para classificar flor de iris em 3 categorias')
st.header('Características da plantas')
col1, col2 = st.columns(2)
with col1:
    st.text("Características da Sépala")
    sepal_l = st.slider('Altura (cm)', 1.0, 8.0, 0.5)
    sepal_w = st.slider('Largura (cm)', 2.0, 4.4, 0.5)

with col2:
    st.text("Características da Pétala")
    petal_l = st.slider('Altura (cm)', 1.0, 7.0, 0.5)
    petal_w = st.slider('Largura (cm)', 0.1, 2.5, 0.5)

st.text('')
#Botão de predição
if st.button('Predição do tipo da flor'):
    result = predict([[sepal_l, sepal_w, petal_l, petal_w]])
    if result == 0:
        st.text('Possível Iris Vetosa')
    elif result == 1:
        st.text('Possível Iris Versicolor')
    elif result == 2:
        st.text('Possível Iris Virginica')
    else:
        st.text('Flor desconhecida')

