"""
This is the main file that contains the Streamlit app ui.
"""

import streamlit as st
import pandas as pd

from blog_generator import BlogGenerator
from blog_manager import BlogManager
from blog_writer import BlogWriter
from utils import format_func


st.set_page_config(
    page_title="AutoBlog: AI Blog Generator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("AI Blog Generator ✨")
st.subheader("Create hundreds of blogs for free with the power of local llms.")

generate_tab, blogs_tab = st.tabs(["Generate", "Blogs"])

blog_writer = BlogWriter()
blog_manager = BlogManager()
blog_generator = BlogGenerator(blog_writer, blog_manager)

with generate_tab:
    general_tab_container = st.container(border=True)
    topic_input = general_tab_container.text_input(
        "Enter the topic for the blog",
        help="Keep the topic short and simple.",
        placeholder="eg. Next.js",
    )
    blog_count_input = general_tab_container.slider("The number of blogs to generate")
    format_blog = general_tab_container.checkbox(
        "Format blog",
        help=(
            "Generated blog may be poorly formatted. Enable this to format the markdown properly. "
            "However, this may take longer, and the length of the blog may change. "
            "Unselect this if you want the blog to be longer."
        ),
    )

    button = general_tab_container.button("Generate")

    if button:
        if topic_input and blog_count_input:
            with st.status("Generating Blogs..."):
                for log in blog_generator.generate_blog(
                    topic_input, blog_count_input, format_blog
                ):
                    st.markdown(log)
        else:
            st.warning("Please enter a topic and the number of blogs to generate")


with blogs_tab:
    # Read all the files inside the blogs folder
    generated_blogs = blog_manager.fetch_stats_for_md_files(directory="blogs")
    df = pd.DataFrame(
        generated_blogs, columns=["Topic", "Blog Title", "Lines", "Words", "Characters"]
    )
    st.dataframe(df)

    select_box = st.selectbox(
        "Select a blog",
        df[["Topic", "Blog Title"]].apply(format_func, axis=1).tolist(),
        index=None,
        placeholder="Choose a blog from the dropdown to view it.",
    )
    if select_box is not None:
        container = st.container(border=True)
        with open(f"blogs/{select_box}", "r", encoding="utf-8") as f:
            blog_content = f.read()
            container.markdown(blog_content)
