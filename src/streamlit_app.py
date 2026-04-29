import streamlit as st


st.write("Most objects")  # df, err, func, keras!
st.write(["st", "is <", 3])

st.text("Fixed width text")
st.markdown("_Markdown_")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.badge("New")
st.html("<p>Hi!</p>")
st.iframe("https://docs.streamlit.io", height=600)


#  = st.sidebar.radio("Select one:", [1, 2])

# Or use "with" notation:
with st.sidebar:
    st.radio("Select one:", [1, 2])
