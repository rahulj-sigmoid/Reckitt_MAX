import streamlit as st

# st.set_page_config(page_title="Business Agents", layout="wide")

st.markdown(
    """
    <div style="text-align: center;">
        <h1>Business Experts</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Create a grid of agent cards
col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.markdown(
        """
        <div style="padding: 10px; border: 1px solid #ddd; border-radius: 10px;">
            <h4>Sherlock</h4>
            <p>Your analytics expert for business intelligence and market insights.</p>
            <br/>
        </div>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """
        <div style="padding: 10px; border: 1px solid #ddd; border-radius: 10px;">
            <h4>Supply Chain</h4>
            <p>Your supply chain specialist for logistics and operations insights.</p>
            <br/>
        </div>
        """,
        unsafe_allow_html=True
    )
with col3:
    st.markdown(
        """
        <div style="padding: 10px; border: 1px solid #ddd; border-radius: 10px;">
            <h4>Sherlock</h4>
            <p>Your analytics expert for business intelligence and market insights.</p>
            <br/>
        </div>
        """,
        unsafe_allow_html=True
    )

