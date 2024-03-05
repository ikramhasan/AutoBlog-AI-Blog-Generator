"""
A module that manages the creation, retrieval, and statistics of blog files.
"""

import glob
import os


class BlogManager:
    """
    A class that manages the creation, retrieval, and statistics of blog files.

    Attributes:
        None

    Methods:
        fetch_existing_blogs: Fetches the names of existing blogs for a given topic.
        save_text_as_markdown: Save the given text as a markdown file with the suggested topic.
        fetch_stats_for_md_files: Retrieve information about Markdown files in a given directory.
    """

    def fetch_existing_blogs(self, topic):
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

    def save_text_as_markdown(self, text, suggested_topic, topic):
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

    def fetch_stats_for_md_files(self, directory):
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
                files_data.append(
                    [topic, os.path.basename(file), lines, words, characters]
                )
        return files_data
