import streamlit as st

st.set_page_config(
    page_title = 'Multipage app',
    page_icon='😒',
)
st.title('Main Page')
st.sidebar.success('select a page above')

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Írj valamit", st.session_state["my_input"])
submit = st.button("Beküldés")
if submit:
    st.session_stat["my_input"] = my_input
    st.write("Amit te írtál: ", my_input)