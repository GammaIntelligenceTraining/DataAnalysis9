import pandas as pd
import plotly.express as px

df = pd.read_csv('estonia-passenger-list.csv', index_col='PassengerId')
df

df.info()

# ### 1. Visualize and analize passengers by countries

# +
country_hist = px.histogram(df,
                            x='Country',
                            height=500,
                            color='Category',
                            barmode='group',
                            log_y=True,
                            color_discrete_sequence=['pink', 'green'],
                            title='Counted Passengers & Crew grouped by Category'
                           )

country_hist

# +
country_sunbirst = px.sunburst(df,
                               path=['Category', 'Country'],
                               height=650,
                               hover_name='Country',
                               color='Survived',
                               color_continuous_scale=px.colors.cyclical.Twilight
                              )

country_sunbirst
# -

df_cat = df.groupby('Category')

country_vc = df_cat.Country.value_counts().to_frame()
country_vc

# ### 2. Visualize and analyze passengers by gender and age

# +
sex_hist = px.histogram(df,
                        height=450,
                        x='Sex',
                        color='Category',
                        color_discrete_sequence=['pink', 'green'],
                        barmode='group',
                        title='Counted Passengers & Crew grouped by Gender'
                       )

sex_hist

# +
age_hist = px.histogram(df,
                        x='Age',
                        color='Category',
                        color_discrete_sequence=['pink', 'green'],
                        height=650,
                        barmode='overlay',
                        facet_row='Sex'
                       )

age_hist

# +
age_treemap = px.treemap(df,
                         height=800,
                         path=[px.Constant('Total'), 'Category', 'Country', 'Sex'],
                         color='Age'
                        )

age_treemap
# -

sex_count = df_cat.Sex.value_counts().to_frame()
sex_count

# ### 3. Group age and make final plot

df['Age_group'] = pd.cut(df.Age, 6, precision=0, labels=['Child', 'Young', 'Adult', 'Mid-life', 'Senior', 'Elderly'])

df.head()

px.histogram(df,
             x='Age_group',
             color='Survived',
             barmode='overlay',
             height=450
            )

# +
final_plot = px.histogram(df,
                          x='Age_group',
                          color='Sex',
                          height=800,
                          facet_col='Survived',
                          facet_row='Category',
                          barmode='group',
                          category_orders={'Age_group': ['Child', 'Young', 'Adult', 'Mid-life', 'Senior', 'Elderly']}
                         )

final_plot
# -

# ### 4. Visualize conclusions

# ### 5. Text variables

# +
history = '''MS Estonia was a cruiseferry built in 1979/80 at the German shipyard Meyer Werft in Papenburg. The ship's 1994 sinking, in the Baltic Sea between Sweden, Åland, Finland and Estonia, was one of the worst maritime disasters of the 20th century. It is the second-deadliest peacetime sinking of a European ship, after the RMS Titanic, and the deadliest peacetime shipwreck to have occurred in European waters, with 852 lives lost. At 6.30pm on 27 September 1994, the ferry MS Estonia – the largest ship then flying the flag of the young Baltic republic, and a symbol of recently regained independence – set sail from Tallinn on a routine overnight crossing to Stockholm. On board were 803 passengers, most of them Swedish, and 186 crew, most of them Estonian. The conditions were rough – force 8 winds and waves up to 6 metres – but not unusual for the Baltic Sea in autumn. All other scheduled ferries were at sea.'''

country_conc = '''Here we can see that most of passengers were from baltic and scandinavian countries and most of crew were from Estonia, Sweden, Russia and Finland. On the sunburst chart the colorbar represents percent of survivors for every country.'''

age_conc = '''There were just about equal males and females on board. Also we can see that average age of passengers was much higher then average age of crew. The country with significant number of passengers and highest mean age is Sweden.'''

final_conc = '''On the plot above we can compare the number of survivals dependent on their category (passenger/crew), age group and gender. Most survived passengers as well as crew were men 19-45 years old. In opposite, almost nobody survived in age group more then 60 y.o. To descry a correlation between age and chance of survive we can plot two bar charts: everage age per country and percent of survivals per country. Countries with less then 4 persons on board are not taken into account as non-significant.'''

country_compare = '''We can approve that the higher average age was - the less representatives of a country survived but here we have some exceptions like Germany, Finland and Estonia.''' 
