"""
Handler for handling markdown operations
"""

import markdown


def get_metadata(content: str) -> dict:
    """
    Get metadata from markdown file
    """
    md = markdown.Markdown(extensions=["meta"])
    md.convert(content)
    return md.Meta  # type: ignore
