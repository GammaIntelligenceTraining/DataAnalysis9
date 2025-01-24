import streamlit as st
from report_template import df, history


st.set_page_config('History', layout='wide')

st.header('MS Estonia History', divider='grey')

col1, col2 = st.columns(2)
col1.write(history)
col2.image('MS_Estonia.jpeg', caption='Sinking of MS Estonia')

st.divider()

def filter_by_category(choice):
    if choice == 'Both':
        filtered_df = df
    else:
        filtered_df = df[df.Category == choice[0]]

    return filtered_df

cat = st.sidebar.radio('Which category to show:',
                       options=['Both', 'Passengers', 'Crew'])

filtered_df = filter_by_category(cat)

country = st.sidebar.multiselect('Which country to show:',
                                 options=filtered_df.Country.unique(),
                                 default=['Estonia', 'Sweden'])

final_df = filtered_df[filtered_df.Country.isin(country)]

st.dataframe(final_df, use_container_width=True)
