"""
Gemini Module
"""
from langchain_google_genai import ChatGoogleGenerativeAI


class Gemini(ChatGoogleGenerativeAI):
    """
    A wrapper for the Gemini class that provides default configuration
    and could be extended with additional methods if needed.

    Args:
        llm_config (dict): Configuration parameters for the language model (e.g., model="gemini-pro")
    """

    def __init__(self, llm_config: dict):
        super().__init__(**llm_config)
