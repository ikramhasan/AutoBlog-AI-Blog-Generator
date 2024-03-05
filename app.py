import time
import re
import glob
import os
import streamlit as st
import pandas as pd
from litellm import completion


def get_ai_completion(text):
    """
    Get AI completion for the given text.

    Args:
        text (str): The input text for AI completion.

    Returns:
        str: The AI-generated completion for the given text.
    """
    response = completion(
        model="ollama/mistral:7b-instruct",
        messages=[{"content": text, "role": "user"}],
        api_base="http://localhost:11434",
        stream=False,
    )

    return response.choices[0].message.content


def fetch_sections_from_outline(outline):
    """
    Fetches sections from an outline.

    Args:
        outline (str): The outline to fetch sections from.

    Returns:
        list: A list of sections extracted from the outline.
    """
    lines = outline.strip().split("\n")
    sections = []

    # Initialize an empty string to hold the current section
    current_section = ""

    for line in lines:
        # Ignore empty lines
        if not line.strip():
            continue
        # If the line starts with a roman numeral, it's a new section
        if re.match(r"^[IVXLCDM]+\.", line):
            # If there's a current section, add it to the sections list
            if current_section:
                sections.append(current_section)
            # Start a new section
            current_section = line.strip()
        # If the line starts with a letter and a period, it's a subsection
        elif re.match(r"^\s+[A-Z]\.", line):
            # Add the subsection to the current section
            current_section += "\n" + line.strip()

    # Add the last section to the sections list
    if current_section:
        sections.append(current_section)

    return sections


def fetch_existing_blogs(topic):
    """
    Fetches the names of existing blogs for a given topic.

    Args:
        topic (str): The topic for which to fetch existing blogs.

    Returns:
        list: A list of existing blog names (without the file extension).
    """
    existing_blogs = []
    folder_path = f"blogs/{topic}"
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".md"):
                existing_blogs.append(file[:-3])  # Remove the file extension
    return existing_blogs


def save_text_as_markdown(text, suggested_topic, topic):
    """
    Save the given text as a markdown file with the suggested topic.

    Args:
        text (str): The text content to be saved as markdown.
        suggested_topic (str): The suggested topic for the markdown file.
        topic (str): The main topic or category for organizing the markdown files.

    Returns:
        None
    """
    # Remove any leading or trailing quotes from suggested_topic if any
    suggested_topic = suggested_topic.strip().strip('"').strip("'")
    # Remove trailing period if any
    if suggested_topic.endswith("."):
        suggested_topic = suggested_topic[:-1]
    folder_path = f"blogs/{topic}"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{suggested_topic}.md")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)


def generate_blog(topic, blog_count, format_blog):
    """
    Generate a blog post based on the given topic.

    Args:
        topic (str): The topic for the blog post.
        blog_count (int): The number of blog posts to generate.
        format_blog (bool): Flag indicating whether to format the blog post.

    Yields:
        str: Each step of the blog generation process.

    Returns:
        None
    """
    blogs = fetch_existing_blogs(topic)
    for i in range(blog_count):
        # Log time to generate each blog
        start_time = time.time()
        blog_titles = ", ".join(blogs)
        suggested_topic = get_ai_completion(
            f"Suggest a topic for a blog post about {topic} in one line. Don't include topics that are similar to these topics: {blog_titles}. Suggest only one topic. Don't write a paragraph. Just one line. Don't mention anything else."
        )
        suggested_topic = suggested_topic.strip().strip('"').strip("'")

        yield f"### Blog {i+1}: {suggested_topic}"
        blogs.append(suggested_topic)
        yield "\n*Generating outline...*"
        outline = get_ai_completion(
            f"Write an outline for a blog post about {suggested_topic}. Don't write a paragraph. Don't mention anything else."
        )
        sections = fetch_sections_from_outline(outline)

        for index, section in enumerate(sections):
            yield f"\n**Section {index+1}: {section}**"

        blog = f"# {suggested_topic}\n\n"

        yield "\n*Generating content for each sections...*"
        for index, section in enumerate(sections):
            yield f"*Section {index+1}: done*"
            content = get_ai_completion(
                f"You are an experience content writer. You are capable of writing captivating, highly informative, seo optimized blogs. I'm going to give you a topic and each section, and you are going to write the content for that section in markdown format. Write a paragraph about this section: {section} on the topic: {suggested_topic}. Just write a paragraph. Don't mention anything else."
            )
            blog += f"\n\n{content}\n\n"

        yield "Blog generation complete."
        yield f"Blog length: {len(blog.split())} words. {len(blog)} characters."
        if format_blog:
            yield "\n*Formatting the blog in proper markdown format...*"
            formatted_blog = get_ai_completion(
                f"Blog: {blog}\n\n\nEnhance the formatting of this markdown blog. Fix indentations, headings, and styles. Don't modify the actual content. Just fix the formatting."
            )
            blog = formatted_blog
            yield f"Formatted blog length: {len(formatted_blog.split())} words. {len(formatted_blog)} characters."

        end_time = time.time()
        elapsed_time = end_time - start_time  # calculate the difference
        elapsed_time_in_minutes = elapsed_time / 60  # convert to minutes
        yield f"**Time taken to generate the blog: {elapsed_time_in_minutes:.2f} minutes.**"
        yield "---"
        save_text_as_markdown(blog, suggested_topic, topic=topic)


def list_md_files(directory):
    """
    Retrieve information about Markdown files in a given directory.

    Args:
        directory (str): The directory path to search for Markdown files.

    Returns:
        list: A list of lists containing information about each Markdown file.
              Each inner list contains the following information:
              - Topic: The topic of the file (derived from the directory structure).
              - Filename: The name of the Markdown file.
              - Lines: The number of lines in the file.
              - Words: The number of words in the file.
              - Characters: The number of characters in the file.
    """
    files_data = []
    for file in glob.glob(f"{directory}/**/*.md", recursive=True):
        with open(file, "r", encoding="utf-8") as file_obj:
            content = file_obj.read()
            words = len(content.split())
            characters = len(content)
            lines = content.count("\n") + 1
            topic = os.path.dirname(file).replace(directory, "").strip("/")
            files_data.append([topic, os.path.basename(file), lines, words, characters])
    return files_data


st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("AI Blog Generator ✨")
st.subheader("Create hundreds of blogs for free with the power of local llms.")

generate_tab, blogs_tab = st.tabs(["Generate", "Blogs"])

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
        help="Generated blog may be poorly formatted. Enable this to format the markdown properly. However, this may take longer, and the length of the blog may change. Unselect this if you want the blog to be longer.",
    )

    button = general_tab_container.button("Generate")

    if button:
        if topic_input and blog_count_input:
            with st.status("Generating Blogs..."):
                for log in generate_blog(topic_input, blog_count_input, format_blog):
                    st.markdown(log)
        else:
            st.warning("Please enter a topic and the number of blogs to generate")


def format_func(row):
    return f"{row['Topic']}/{row['Blog Title']}"


with blogs_tab:
    # Read all the files inside the blogs folder
    generated_blogs = list_md_files("blogs")
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
