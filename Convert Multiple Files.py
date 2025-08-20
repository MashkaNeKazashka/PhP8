# Repository: python-markdown-to-html


import markdown
import os

def batch_convert(directory):
    """Convert all Markdown files in a directory to HTML."""
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, filename.replace(".md", ".html"))
            with open(input_path, 'r') as file:
                text = file.read()
                html = markdown.markdown(text)
            with open(output_path, 'w') as output_file:
                output_file.write(html)
            print(f"Converted {input_path} to {output_path}")

# Example usage
batch_convert("/path/to/markdown/files")
