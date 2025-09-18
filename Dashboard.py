import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
    layout= "wide"
)

# Sidebar configuration
st.sidebar.image("assets/logo.png")
st.sidebar.caption('Welcome to the Heart Prediction - A Heart Failure Prediction Platform!')
page = st.sidebar.radio('Go to', ['Dashboard', 'Prediction', 'About'])

# # Page information

if page == 'Dashboard':
    st.title('Dashboard')
    st.caption('A simple demo dashboard for individual assignment 2.')
    left, right = st.columns([1,2], gap ='large')
    with left:
        st.subheader("Controls")
        n_points = st.slider("Number of data points", 10, 500, 250, step=10)
        dist = st.selectbox("Distribution", ["Normal", "Uniform"])
        label = st.text_input("Series label", value="My Series")

        rng = np.random.default_rng(9771)
        x = np.arange(n_points)
        y = rng.normal(0, 1, n_points) if dist == "Normal" else rng.uniform(-1, 1, n_points)
        df = pd.DataFrame({"x": x, "y": y, "label": label})

    with right:
        st.subheader("Data & Chart")
        st.dataframe(df.head(), use_container_width=True)

        chart = (
            alt.Chart(df)
            .mark_line()
            .encode(x="x:Q", y="y:Q", tooltip=["x", "y"])
        )
        st.altair_chart(chart, use_container_width=True)




elif page == 'Prediction':
    st.title('Heart Failure Prediction')
    st.caption('Fill in the fields on right and click Submit to get a simple risk estimate.')
    left, right = st.columns([1,2], gap ='large')
    with left:
        st.subheader('👉 Tips!')
        st.write('This is a simplified model for demonstration purposes only (not for clinical use).')

    with right:
        st.subheader('Patient Information')
        age = st.number_input("Age (years)", min_value=0, max_value=120, value=50, step=1)
        sex = st.selectbox("Sex", ["Female", "Male"])
        chol = st.number_input("Serum cholesterol (mg/dL)", min_value=100, max_value=600, value=200, step=1)
        submitted = st.button("Submit")
        if submitted:
            st.success("Form submitted! (Demo only, no real prediction)")



elif page == 'About':
    st.title("Xue Wu")
    st.markdown("""
    **About this project**

During the DSHI course, I built a simple multipage Streamlit dashboard to practice end-to-end data product skills.  
The app includes a Dashboard page with interactive input widgets, a small synthetic dataset generated with NumPy, and a clean Altair chart for quick visual exploration.  
A Prediction page demonstrates how a basic form could collect patient-level inputs for a toy risk estimate (not for clinical use).  
My focus was clarity, reproducibility, and version control: I organized the repository, wrote a self-explanatory README with screenshots, and used incremental commits with descriptive messages.  
This mini project reflects a typical data science workflow—parameterization, tabular inspection, and visualization—and serves as a starting point for future health informatics prototypes.
    """)