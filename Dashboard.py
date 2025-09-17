import streamlit as st

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
if page == 'Prediction':
    st.title('Heart Failure Prediction')
    st.caption('Fill in the fields on right and click Submit to get a simple risk estimate.')
    left, right = st.columns([1,2], gap ='large')
    with left:
        st.subheader('Tips!')
        st.write('This is a simplified model for decomstration purposes only (not for clinical use).')

    with right:
        st.subheader('Patient Information')

        


elif page == 'About':
    st.title("Welcome to PROHI Dashboard!")
    st.caption("A simple demo dashboard for individual assignment 2.")

    st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
    )

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

# # DATAFRAME MANAGEMENT
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# # Add a slider to the sidebar:
add_slider = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
 )
