"""
A module that represents a blog writer.
"""

from litellm import completion


class BlogWriter:
    """
    A class that represents a blog writer.

    Attributes:
        None

    Methods:
        write(text): Get AI completion for the given text.
    """

    def write(self, text):
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
