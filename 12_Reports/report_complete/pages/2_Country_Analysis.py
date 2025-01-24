import streamlit as st
from report_template import country_hist, country_sunbirst, country_vc, country_conc

st.set_page_config(page_title='Country_Analysis', layout='wide')

st.header('Analysis of Passengers and Crew by Country', divider='gray')

st.plotly_chart(country_hist, use_container_width=True)
st.plotly_chart(country_sunbirst, use_container_width=True)

exp = st.expander('Conclusion')
with exp:
    col1, col2 = st.columns(2)
    col1.write(country_conc)
    col2.table(country_vc)