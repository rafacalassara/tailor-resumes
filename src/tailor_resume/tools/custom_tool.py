from crewai_tools import BaseTool, tool


class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


@tool
def create_markdown_file(content: str, filename: str) -> str:
    """
    Create a markdown file with the given content and filename.

    Args:
        content (str): The content to write to the markdown file.
        filename (str): The name of the markdown file (without extension).

    Returns:
        str: A message indicating success or failure.
    """
    try:
        # Ensure filename has .md extension
        if not filename.endswith(".md"):
            filename += ".md"

        with open(filename, 'w') as md_file:
            md_file.write(content)

        return f"Markdown file '{filename}' created successfully."
    except Exception as e:
        return f"Failed to create markdown file: {str(e)}"
