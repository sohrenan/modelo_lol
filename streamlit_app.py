import os
import pickle

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Previsão Resultados CBLOL 2024",
    page_icon="images/cblol.ico",  # Provide the path to your favicon
    layout="centered"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css('styles.css')

current_dir = os.path.dirname(__file__)
times = pd.read_csv('data/times.csv')
log_model_path = 'model/rf.sav'
with open(log_model_path, 'rb') as file:
    log_model = pickle.load(file)


def criar_dados(times, blue_team, red_team):
    data = {}

    kills_adc_blue = int(times.loc[times['nome_time'] == blue_team]['kills_adc'].values[0])
    kills_adc_red = int(times.loc[times['nome_time'] == red_team]['kills_adc'].values[0])
    deaths_adc_blue = int(times.loc[times['nome_time'] == blue_team]['deaths_adc'].values[0])
    deaths_adc_red = int(times.loc[times['nome_time'] == red_team]['deaths_adc'].values[0])
    assists_adc_blue = int(times.loc[times['nome_time'] == blue_team]['assists_adc'].values[0])
    assists_adc_red = int(times.loc[times['nome_time'] == red_team]['assists_adc'].values[0])
    cs_adc_blue = int(times.loc[times['nome_time'] == blue_team]['cs_adc'].values[0])
    cs_adc_red = int(times.loc[times['nome_time'] == red_team]['cs_adc'].values[0])
    csm_adc_blue = int(times.loc[times['nome_time'] == blue_team]['csm_adc'].values[0])
    csm_adc_red = int(times.loc[times['nome_time'] == red_team]['csm_adc'].values[0])
    gold_adc_blue = int(times.loc[times['nome_time'] == blue_team]['gold_adc'].values[0])
    gold_adc_red = int(times.loc[times['nome_time'] == red_team]['gold_adc'].values[0])
    gpm_adc_blue = int(times.loc[times['nome_time'] == blue_team]['gpm_adc'].values[0])
    gpm_adc_red = int(times.loc[times['nome_time'] == red_team]['gpm_adc'].values[0])
    dmg_adc_blue = int(times.loc[times['nome_time'] == blue_team]['dmg_adc'].values[0])
    dmg_adc_red = int(times.loc[times['nome_time'] == red_team]['dmg_adc'].values[0])
    dmgm_adc_blue = int(times.loc[times['nome_time'] == blue_team]['dmgm_adc'].values[0])
    dmgm_adc_red = int(times.loc[times['nome_time'] == red_team]['dmgm_adc'].values[0])
    kpar_adc_blue = int(times.loc[times['nome_time'] == blue_team]['kpar_adc'].values[0])
    kpar_adc_red = int(times.loc[times['nome_time'] == red_team]['kpar_adc'].values[0])
    ks_adc_blue = int(times.loc[times['nome_time'] == blue_team]['ks_adc'].values[0])
    ks_adc_red = int(times.loc[times['nome_time'] == red_team]['ks_adc'].values[0])
    gs_adc_blue = int(times.loc[times['nome_time'] == blue_team]['gs_adc'].values[0])
    gs_adc_red = int(times.loc[times['nome_time'] == red_team]['gs_adc'].values[0])

    kills_sup_blue = int(times.loc[times['nome_time'] == blue_team]['kills_sup'].values[0])
    kills_sup_red = int(times.loc[times['nome_time'] == red_team]['kills_sup'].values[0])
    deaths_sup_blue = int(times.loc[times['nome_time'] == blue_team]['deaths_sup'].values[0])
    deaths_sup_red = int(times.loc[times['nome_time'] == red_team]['deaths_sup'].values[0])
    assists_sup_blue = int(times.loc[times['nome_time'] == blue_team]['assists_sup'].values[0])
    assists_sup_red = int(times.loc[times['nome_time'] == red_team]['assists_sup'].values[0])
    cs_sup_blue = int(times.loc[times['nome_time'] == blue_team]['cs_sup'].values[0])
    cs_sup_red = int(times.loc[times['nome_time'] == red_team]['cs_sup'].values[0])
    csm_sup_blue = int(times.loc[times['nome_time'] == blue_team]['csm_sup'].values[0])
    csm_sup_red = int(times.loc[times['nome_time'] == red_team]['csm_sup'].values[0])
    gold_sup_blue = int(times.loc[times['nome_time'] == blue_team]['gold_sup'].values[0])
    gold_sup_red = int(times.loc[times['nome_time'] == red_team]['gold_sup'].values[0])
    gpm_sup_blue = int(times.loc[times['nome_time'] == blue_team]['gpm_sup'].values[0])
    gpm_sup_red = int(times.loc[times['nome_time'] == red_team]['gpm_sup'].values[0])
    dmg_sup_blue = int(times.loc[times['nome_time'] == blue_team]['dmg_sup'].values[0])
    dmg_sup_red = int(times.loc[times['nome_time'] == red_team]['dmg_sup'].values[0])
    dmgm_sup_blue = int(times.loc[times['nome_time'] == blue_team]['dmgm_sup'].values[0])
    dmgm_sup_red = int(times.loc[times['nome_time'] == red_team]['dmgm_sup'].values[0])
    kpar_sup_blue = int(times.loc[times['nome_time'] == blue_team]['kpar_sup'].values[0])
    kpar_sup_red = int(times.loc[times['nome_time'] == red_team]['kpar_sup'].values[0])
    ks_sup_blue = int(times.loc[times['nome_time'] == blue_team]['ks_sup'].values[0])
    ks_sup_red = int(times.loc[times['nome_time'] == red_team]['ks_sup'].values[0])
    gs_sup_blue = int(times.loc[times['nome_time'] == blue_team]['gs_sup'].values[0])
    gs_sup_red = int(times.loc[times['nome_time'] == red_team]['gs_sup'].values[0])

    kills_mid_blue = int(times.loc[times['nome_time'] == blue_team]['kills_mid'].values[0])
    kills_mid_red = int(times.loc[times['nome_time'] == red_team]['kills_mid'].values[0])
    deaths_mid_blue = int(times.loc[times['nome_time'] == blue_team]['deaths_mid'].values[0])
    deaths_mid_red = int(times.loc[times['nome_time'] == red_team]['deaths_mid'].values[0])
    assists_mid_blue = int(times.loc[times['nome_time'] == blue_team]['assists_mid'].values[0])
    assists_mid_red = int(times.loc[times['nome_time'] == red_team]['assists_mid'].values[0])
    cs_mid_blue = int(times.loc[times['nome_time'] == blue_team]['cs_mid'].values[0])
    cs_mid_red = int(times.loc[times['nome_time'] == red_team]['cs_mid'].values[0])
    csm_mid_blue = int(times.loc[times['nome_time'] == blue_team]['csm_mid'].values[0])
    csm_mid_red = int(times.loc[times['nome_time'] == red_team]['csm_mid'].values[0])
    gold_mid_blue = int(times.loc[times['nome_time'] == blue_team]['gold_mid'].values[0])
    gold_mid_red = int(times.loc[times['nome_time'] == red_team]['gold_mid'].values[0])
    gpm_mid_blue = int(times.loc[times['nome_time'] == blue_team]['gpm_mid'].values[0])
    gpm_mid_red = int(times.loc[times['nome_time'] == red_team]['gpm_mid'].values[0])
    dmg_mid_blue = int(times.loc[times['nome_time'] == blue_team]['dmg_mid'].values[0])
    dmg_mid_red = int(times.loc[times['nome_time'] == red_team]['dmg_mid'].values[0])
    dmgm_mid_blue = int(times.loc[times['nome_time'] == blue_team]['dmgm_mid'].values[0])
    dmgm_mid_red = int(times.loc[times['nome_time'] == red_team]['dmgm_mid'].values[0])
    kpar_mid_blue = int(times.loc[times['nome_time'] == blue_team]['kpar_mid'].values[0])
    kpar_mid_red = int(times.loc[times['nome_time'] == red_team]['kpar_mid'].values[0])
    ks_mid_blue = int(times.loc[times['nome_time'] == blue_team]['ks_mid'].values[0])
    ks_mid_red = int(times.loc[times['nome_time'] == red_team]['ks_mid'].values[0])
    gs_mid_blue = int(times.loc[times['nome_time'] == blue_team]['gs_mid'].values[0])
    gs_mid_red = int(times.loc[times['nome_time'] == red_team]['gs_mid'].values[0])

    kills_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['kills_jungle'].values[0])
    kills_jungle_red = int(times.loc[times['nome_time'] == red_team]['kills_jungle'].values[0])
    deaths_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['deaths_jungle'].values[0])
    deaths_jungle_red = int(times.loc[times['nome_time'] == red_team]['deaths_jungle'].values[0])
    assists_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['assists_jungle'].values[0])
    assists_jungle_red = int(times.loc[times['nome_time'] == red_team]['assists_jungle'].values[0])
    cs_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['cs_jungle'].values[0])
    cs_jungle_red = int(times.loc[times['nome_time'] == red_team]['cs_jungle'].values[0])
    csm_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['csm_jungle'].values[0])
    csm_jungle_red = int(times.loc[times['nome_time'] == red_team]['csm_jungle'].values[0])
    gold_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['gold_jungle'].values[0])
    gold_jungle_red = int(times.loc[times['nome_time'] == red_team]['gold_jungle'].values[0])
    gpm_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['gpm_jungle'].values[0])
    gpm_jungle_red = int(times.loc[times['nome_time'] == red_team]['gpm_jungle'].values[0])
    dmg_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['dmg_jungle'].values[0])
    dmg_jungle_red = int(times.loc[times['nome_time'] == red_team]['dmg_jungle'].values[0])
    dmgm_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['dmgm_jungle'].values[0])
    dmgm_jungle_red = int(times.loc[times['nome_time'] == red_team]['dmgm_jungle'].values[0])
    kpar_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['kpar_jungle'].values[0])
    kpar_jungle_red = int(times.loc[times['nome_time'] == red_team]['kpar_jungle'].values[0])
    ks_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['ks_jungle'].values[0])
    ks_jungle_red = int(times.loc[times['nome_time'] == red_team]['ks_jungle'].values[0])
    gs_jungle_blue = int(times.loc[times['nome_time'] == blue_team]['gs_jungle'].values[0])
    gs_jungle_red = int(times.loc[times['nome_time'] == red_team]['gs_jungle'].values[0])

    kills_top_blue = int(times.loc[times['nome_time'] == blue_team]['kills_top'].values[0])
    kills_top_red = int(times.loc[times['nome_time'] == red_team]['kills_top'].values[0])
    deaths_top_blue = int(times.loc[times['nome_time'] == blue_team]['deaths_top'].values[0])
    deaths_top_red = int(times.loc[times['nome_time'] == red_team]['deaths_top'].values[0])
    assists_top_blue = int(times.loc[times['nome_time'] == blue_team]['assists_top'].values[0])
    assists_top_red = int(times.loc[times['nome_time'] == red_team]['assists_top'].values[0])
    cs_top_blue = int(times.loc[times['nome_time'] == blue_team]['cs_top'].values[0])
    cs_top_red = int(times.loc[times['nome_time'] == red_team]['cs_top'].values[0])
    csm_top_blue = int(times.loc[times['nome_time'] == blue_team]['csm_top'].values[0])
    csm_top_red = int(times.loc[times['nome_time'] == red_team]['csm_top'].values[0])
    gold_top_blue = int(times.loc[times['nome_time'] == blue_team]['gold_top'].values[0])
    gold_top_red = int(times.loc[times['nome_time'] == red_team]['gold_top'].values[0])
    gpm_top_blue = int(times.loc[times['nome_time'] == blue_team]['gpm_top'].values[0])
    gpm_top_red = int(times.loc[times['nome_time'] == red_team]['gpm_top'].values[0])
    dmg_top_blue = int(times.loc[times['nome_time'] == blue_team]['dmg_top'].values[0])
    dmg_top_red = int(times.loc[times['nome_time'] == red_team]['dmg_top'].values[0])
    dmgm_top_blue = int(times.loc[times['nome_time'] == blue_team]['dmgm_top'].values[0])
    dmgm_top_red = int(times.loc[times['nome_time'] == red_team]['dmgm_top'].values[0])
    kpar_top_blue = int(times.loc[times['nome_time'] == blue_team]['kpar_top'].values[0])
    kpar_top_red = int(times.loc[times['nome_time'] == red_team]['kpar_top'].values[0])
    ks_top_blue = int(times.loc[times['nome_time'] == blue_team]['ks_top'].values[0])
    ks_top_red = int(times.loc[times['nome_time'] == red_team]['ks_top'].values[0])
    gs_top_blue = int(times.loc[times['nome_time'] == blue_team]['gs_top'].values[0])
    gs_top_red = int(times.loc[times['nome_time'] == red_team]['gs_top'].values[0])

    data['time_blue'] = times.loc[times['nome_time'] == blue_team]['nome_time'].values[0]
    data['time_red'] = times.loc[times['nome_time'] == red_team]['nome_time'].values[0]

    data['kills_adc_blue'] = kills_adc_blue
    data['kills_adc_red'] = kills_adc_red
    data['deaths_adc_blue'] = deaths_adc_blue
    data['deaths_adc_red'] = deaths_adc_red
    data['assists_adc_blue'] = assists_adc_blue
    data['assists_adc_red'] = assists_adc_red
    data['cs_adc_blue'] = cs_adc_blue
    data['cs_adc_red'] = cs_adc_red
    data['csm_adc_blue'] = csm_adc_blue
    data['csm_adc_red'] = csm_adc_red
    data['gold_adc_blue'] = gold_adc_blue
    data['gold_adc_red'] = gold_adc_red
    data['gpm_adc_blue'] = gpm_adc_blue
    data['gpm_adc_red'] = gpm_adc_red
    data['dmg_adc_blue'] = dmg_adc_blue
    data['dmg_adc_red'] = dmg_adc_red
    data['dmgm_adc_blue'] = dmgm_adc_blue
    data['dmgm_adc_red'] = dmgm_adc_red
    data['kpar_adc_blue'] = kpar_adc_blue
    data['kpar_adc_red'] = kpar_adc_red
    data['ks_adc_blue'] = ks_adc_blue
    data['ks_adc_red'] = ks_adc_red
    data['gs_adc_blue'] = gs_adc_blue
    data['gs_adc_red'] = gs_adc_red

    data['kills_sup_blue'] = kills_sup_blue
    data['kills_sup_red'] = kills_sup_red
    data['deaths_sup_blue'] = deaths_sup_blue
    data['deaths_sup_red'] = deaths_sup_red
    data['assists_sup_blue'] = assists_sup_blue
    data['assists_sup_red'] = assists_sup_red
    data['cs_sup_blue'] = cs_sup_blue
    data['cs_sup_red'] = cs_sup_red
    data['csm_sup_blue'] = csm_sup_blue
    data['csm_sup_red'] = csm_sup_red
    data['gold_sup_blue'] = gold_sup_blue
    data['gold_sup_red'] = gold_sup_red
    data['gpm_sup_blue'] = gpm_sup_blue
    data['gpm_sup_red'] = gpm_sup_red
    data['dmg_sup_blue'] = dmg_sup_blue
    data['dmg_sup_red'] = dmg_sup_red
    data['dmgm_sup_blue'] = dmgm_sup_blue
    data['dmgm_sup_red'] = dmgm_sup_red
    data['kpar_sup_blue'] = kpar_sup_blue
    data['kpar_sup_red'] = kpar_sup_red
    data['ks_sup_blue'] = ks_sup_blue
    data['ks_sup_red'] = ks_sup_red
    data['gs_sup_blue'] = gs_sup_blue
    data['gs_sup_red'] = gs_sup_red

    data['kills_mid_blue'] = kills_mid_blue
    data['kills_mid_red'] = kills_mid_red
    data['deaths_mid_blue'] = deaths_mid_blue
    data['deaths_mid_red'] = deaths_mid_red
    data['assists_mid_blue'] = assists_mid_blue
    data['assists_mid_red'] = assists_mid_red
    data['cs_mid_blue'] = cs_mid_blue
    data['cs_mid_red'] = cs_mid_red
    data['csm_mid_blue'] = csm_mid_blue
    data['csm_mid_red'] = csm_mid_red
    data['gold_mid_blue'] = gold_mid_blue
    data['gold_mid_red'] = gold_mid_red
    data['gpm_mid_blue'] = gpm_mid_blue
    data['gpm_mid_red'] = gpm_mid_red
    data['dmg_mid_blue'] = dmg_mid_blue
    data['dmg_mid_red'] = dmg_mid_red
    data['dmgm_mid_blue'] = dmgm_mid_blue
    data['dmgm_mid_red'] = dmgm_mid_red
    data['kpar_mid_blue'] = kpar_mid_blue
    data['kpar_mid_red'] = kpar_mid_red
    data['ks_mid_blue'] = ks_mid_blue
    data['ks_mid_red'] = ks_mid_red
    data['gs_mid_blue'] = gs_mid_blue
    data['gs_mid_red'] = gs_mid_red

    data['kills_jungle_blue'] = kills_jungle_blue
    data['kills_jungle_red'] = kills_jungle_red
    data['deaths_jungle_blue'] = deaths_jungle_blue
    data['deaths_jungle_red'] = deaths_jungle_red
    data['assists_jungle_blue'] = assists_jungle_blue
    data['assists_jungle_red'] = assists_jungle_red
    data['cs_jungle_blue'] = cs_jungle_blue
    data['cs_jungle_red'] = cs_jungle_red
    data['csm_jungle_blue'] = csm_jungle_blue
    data['csm_jungle_red'] = csm_jungle_red
    data['gold_jungle_blue'] = gold_jungle_blue
    data['gold_jungle_red'] = gold_jungle_red
    data['gpm_jungle_blue'] = gpm_jungle_blue
    data['gpm_jungle_red'] = gpm_jungle_red
    data['dmg_jungle_blue'] = dmg_jungle_blue
    data['dmg_jungle_red'] = dmg_jungle_red
    data['dmgm_jungle_blue'] = dmgm_jungle_blue
    data['dmgm_jungle_red'] = dmgm_jungle_red
    data['kpar_jungle_blue'] = kpar_jungle_blue
    data['kpar_jungle_red'] = kpar_jungle_red
    data['ks_jungle_blue'] = ks_jungle_blue
    data['ks_jungle_red'] = ks_jungle_red
    data['gs_jungle_blue'] = gs_jungle_blue
    data['gs_jungle_red'] = gs_jungle_red

    data['kills_top_blue'] = kills_top_blue
    data['kills_top_red'] = kills_top_red
    data['deaths_top_blue'] = deaths_top_blue
    data['deaths_top_red'] = deaths_top_red
    data['assists_top_blue'] = assists_top_blue
    data['assists_top_red'] = assists_top_red
    data['cs_top_blue'] = cs_top_blue
    data['cs_top_red'] = cs_top_red
    data['csm_top_blue'] = csm_top_blue
    data['csm_top_red'] = csm_top_red
    data['gold_top_blue'] = gold_top_blue
    data['gold_top_red'] = gold_top_red
    data['gpm_top_blue'] = gpm_top_blue
    data['gpm_top_red'] = gpm_top_red
    data['dmg_top_blue'] = dmg_top_blue
    data['dmg_top_red'] = dmg_top_red
    data['dmgm_top_blue'] = dmgm_top_blue
    data['dmgm_top_red'] = dmgm_top_red
    data['kpar_top_blue'] = kpar_top_blue
    data['kpar_top_red'] = kpar_top_red
    data['ks_top_blue'] = ks_top_blue
    data['ks_top_red'] = ks_top_red
    data['gs_top_blue'] = gs_top_blue
    data['gs_top_red'] = gs_top_red

    final = pd.DataFrame([data])
    final.drop(['time_blue', 'time_red'], axis=1, inplace=True)
    return final


def main():
    # Get list of valid team names
    team_names = times['nome_time'].tolist()

    with st.container():
        st.image('images/cblol.png')
    with st.container():
        st.empty()
    with st.container():
        st.empty()

    col1, col2,col3 = st.columns([2, 1, 2])



    with col1:
        st.markdown("<h1 style='text-align: center;font-size:40px;'>Red Side</h1>", unsafe_allow_html=True)
        red_team = st.selectbox('Quem joga Red Side?', team_names)



    with col3:
        st.markdown("<h1 style='text-align: center;font-size:40px;'>Blue Side</h1>", unsafe_allow_html=True)
        blue_team = st.selectbox('Quem joga Blue Side?', team_names)




    with st.container():
        st.empty()

    left_column, center_column, right_column = st.columns([2.3, 1, 2])
    with center_column:
        st.empty()
        predict_button = st.button('Prever')



    if predict_button:
        prediction_result, proba_red, proba_blue = predict_survival(blue_team, red_team)
        st.write(f'<span text-align: center>A probabilidade do time {blue_team} ganhar é de {proba_blue:.2f}%</span>', unsafe_allow_html=True)
        st.write(f'A probabilidade do time {red_team} ganhar é de {proba_red:.2f}%', unsafe_allow_html=True)
        if prediction_result == 1:
            st.write(f'<span style="font-size:50px; color:blue">Vitória do Time Azul</span>',
                     unsafe_allow_html=True)
        if prediction_result == 0:
            st.write(f'<span style="font-size:50px; color:red">Vitória do Time Vermelho</span>',
                     unsafe_allow_html=True)


def predict_survival(blue_team, red_team):
    to_predict = criar_dados(times, blue_team, red_team)

    result = log_model.predict(to_predict)
    proba_red = log_model.predict_proba(to_predict)[0][0] * 100
    proba_blue = log_model.predict_proba(to_predict)[0][1] * 100

    return result, proba_red, proba_blue

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


if __name__ == '__main__':

    main()
