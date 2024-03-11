import streamlit as st
import os
import pandas as pd
import pickle
import sklearn


current_dir = os.path.dirname(__file__)

log_model_path = os.path.join(current_dir, 'lol.sav')
with open(log_model_path, 'rb') as file:
    log_model = pickle.load(file)

data_1 = {'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          'nome': ['vivo', 'pain', 'keyd', 'vti', 'intz', 'skt', 'soh', 'red', 'cnb', 'furia'],
          'avg_creep': [10, 24, 54, 22, 14, 55, 67, 12, 90, 100]}
data_2 = {'blue_side_id': [2, 4, 5, 7], 'red_side_id': [1, 3, 4, 8], 'blue_win': [1, 0, 0, 1]}

times = pd.DataFrame(data_1)
times['id'] = times['id'].astype(int)
times['avg_creep'] = times['avg_creep'].astype(int)

partidas = pd.DataFrame(data_2)
partidas['blue_side_id'] = partidas['blue_side_id'].astype(int)
partidas['red_side_id'] = partidas['red_side_id'].astype(int)
partidas['blue_win'] = partidas['blue_win'].astype(int)


def criar_dados(times, blue_team, red_team):
    data = {}

    blue_side_avg_creep = int(times.loc[times['nome'] == blue_team]['avg_creep'].values[0])
    red_side_avg_creep = int(times.loc[times['nome'] == red_team]['avg_creep'].values[0])

    data['blue_side_avg_creep'] = [blue_side_avg_creep]
    data['red_side_avg_creep'] = [red_side_avg_creep]
    final = pd.DataFrame(data)
    return final


def main():
    # Get list of valid team names
    team_names = times['nome'].tolist()

    col1, col2 = st.columns(2)

    with col1:
        st.header('Time Vermelho')
        red_team = st.selectbox('Quem joga no time vermelho?', team_names)

    with col2:
        st.header('Time Azul')
        blue_team = st.selectbox('Quem joga no time azul?', team_names)

    predict_button = st.button('Prever')

    if predict_button:
        prediction_result, proba_red, proba_blue = predict_survival(blue_team, red_team)
        st.write(f'A probabilidade do time {blue_team} ganhar é de {proba_blue:.2f}', unsafe_allow_html=True)
        st.write(f'A probabilidade do time {red_team} ganhar é de {proba_red:.2f}', unsafe_allow_html=True)
        if prediction_result == 1:
            st.write('**resultado:**', f'<span style="font-size:50px; color:blue">Vitória do Time Azul</span>',
                     unsafe_allow_html=True)
        if prediction_result == 0:
            st.write('**resultado:**', f'<span style="font-size:50px; color:red">Vitória do Time Vermelho</span>',
                     unsafe_allow_html=True)


def predict_survival(blue_team, red_team):
    to_predict = criar_dados(times, blue_team, red_team)

    result = log_model.predict(to_predict)
    proba_red = log_model.predict_proba(to_predict)[0][0] * 100
    proba_blue = log_model.predict_proba(to_predict)[0][1] * 100

    return result, proba_red, proba_blue


if __name__ == '__main__':
    st.markdown(
        """
        <style>
        body {
            color: white;
            background-color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    main()
