import streamlit as st
import filefunc

checkList = filefunc.read_todos_file()


def add_item():
    new_item = st.session_state["new_item"] + "\n"
    checkList.append(new_item)
    filefunc.update_todos_file(checkList)


st.title("Checklist of things")


try:
    for index, item in enumerate(checkList):
        checkbox = st.checkbox(item, key=item+str(index))
        if checkbox:
            checkList.pop(index)
            filefunc.update_todos_file(checkList)
            del st.session_state[item+str(index)]
            st.experimental_rerun()
except IndexError:
    st.write("There are no items in checklist")

st.text_input(label="", placeholder="Add a new item",
              on_change=add_item, key="new_item")

st.session_state