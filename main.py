import streamlit as st
st.title("Akash chaudhary")

st.write("MSC DSAI")
st.header("python")
st.markdown('Streamlit is **_really_ cool**.')

import  pandas as pd
import numpy as np






chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

import pandas as pd
import numpy as  np





chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

