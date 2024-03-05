"""
A module that generates blog posts based on a given topic.
"""

import re
import time
from blog_manager import BlogManager
from blog_writer import BlogWriter


class BlogGenerator:
    """
    A class that generates blog posts based on given topics.

    Args:
        blog_writer (object): An instance of the blog writer class.
        blog_manager (object): An instance of the blog manager class.

    Attributes:
        blog_writer (BlogWriter): An instance of the blog writer class.
        blog_manager (BlogManager): An instance of the blog manager class.
    """

    def __init__(self, blog_writer: BlogWriter, blog_manager: BlogManager):
        self.blog_writer = blog_writer
        self.blog_manager = blog_manager

    def fetch_sections_from_outline(self, outline):
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

    def generate_blog(self, topic, blog_count, format_blog):
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
        blogs = self.blog_manager.fetch_existing_blogs(topic)
        for i in range(blog_count):
            # Log time to generate each blog
            start_time = time.time()
            blog_titles = ", ".join(blogs)
            suggested_topic = self.blog_writer.write(
                (
                    f"Suggest a topic for a blog post about {topic} in one line. "
                    f"Don't include topics that are similar to these topics: {blog_titles}. "
                    "Suggest only one topic. Don't write a paragraph. Just one line. "
                    "Don't mention anything else."
                )
            )
            suggested_topic = suggested_topic.strip().strip('"').strip("'")

            yield f"### Blog {i+1}: {suggested_topic}"
            blogs.append(suggested_topic)
            yield "\n*Generating outline...*"
            outline = self.blog_writer.write(
                (
                    f"Write an outline for a blog post about {suggested_topic}. "
                    "Don't write a paragraph. Don't mention anything else."
                )
            )
            sections = self.fetch_sections_from_outline(outline)

            for index, section in enumerate(sections):
                yield f"\n**Section {index+1}: {section}**"

            blog = f"# {suggested_topic}\n\n"

            yield "\n*Generating content for each sections...*"
            for index, section in enumerate(sections):
                yield f"*Section {index+1}: done*"
                content = self.blog_writer.write(
                    (
                        "You are an experienced content writer. "
                        "You are capable of writing captivating, highly informative, "
                        "seo optimized blogs. I'm going to give you a topic and section, and "
                        "you are going to write the content for that section in markdown format. "
                        f"Write a paragraph about this section: {section} on the topic: "
                        f"{suggested_topic}. Just write a paragraph. Don't mention anything else."
                    )
                )
                blog += f"\n\n{content}\n\n"

            yield "Blog generation complete."
            yield f"Blog length: {len(blog.split())} words. {len(blog)} characters."
            if format_blog:
                yield "\n*Formatting the blog in proper markdown format...*"
                formatted_blog = self.blog_writer.write(
                    (
                        f"Blog: {blog}\n\n\nEnhance the formatting of this markdown blog. "
                        "Fix indentations, headings, and styles. Don't modify the actual content. "
                        "Just fix the formatting."
                    )
                )
                blog = formatted_blog
                yield (
                    f"Formatted blog length: {len(formatted_blog.split())} words. "
                    f"{len(formatted_blog)} characters."
                )

            end_time = time.time()
            elapsed_time = end_time - start_time  # calculate the difference
            elapsed_time_in_minutes = elapsed_time / 60  # convert to minutes
            yield f"**Time taken to generate the blog: {elapsed_time_in_minutes:.2f} minutes.**"
            yield "---"
            self.blog_manager.save_text_as_markdown(blog, suggested_topic, topic=topic)
