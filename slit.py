import pandas as pd
import numpy as np

import streamlit as st

st.title('Uber pickups in NYC')

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 6, 5],
  'second column': [10, 20, 30, 40]
})

df

# st.write("hi. Here's our first attempt at using data to create a table:")
# st.table(df)
# st.dataframe(df)


dataframe = pd.DataFrame(np.random.randn(10, 20))
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=(f'col {i}' for i in range(20)))
# st.dataframe(dataframe)
st.dataframe(dataframe.style.highlight_max(axis=0))
st.line_chart(dataframe)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [45.8, 9.06],
#     columns=['lat', 'lon'])

# z = 5

# z = st.slider('zoom')  # 👈 this is a widget
# st.write(z, 'squared is', z**2)



# st.map(map_data, zoom=z, use_container_width=True)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
df['second column'][option]

st.write(st.checkbox('Show dataframe'))

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
