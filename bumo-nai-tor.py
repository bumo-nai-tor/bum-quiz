import streamlit as st

st.title("Bum Rating Quiz")

ace = st.text_input("is ace a bum:")

if ace in ("lowkey", "yes", "perhaps", "ofc", "idk"):
    st.write("yeah u get it")
else:
    st.write("something someone with 67 iq would say")

ace2 = st.text_input("how much of a bum is he:")
if ace2 in ("hes a pretty big bum", "lowkey a big bum", "bum enough"):
    st.write("faaacts")
else:
    st.write("your tweaking on fahads soul")


sami = st.text_input("is sami a good artist:")
if sami in ("yes yes my bro", "yeah", "i think so", "duh", "yes"):
    st.write("facts!")
else:
    st.write("boy what the hell boy.")

