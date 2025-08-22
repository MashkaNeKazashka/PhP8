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
            
def convert_markdown_with_template(file_path, template_path):
    with open(template_path, 'r') as tpl:
        template = tpl.read()
    with open(file_path, 'r') as file:
        text = file.read()
        html = markdown.markdown(text)
        output_html = template.replace("{{content}}", html)
        output_path = file_path.replace('.md', '.html')
        with open(output_path, 'w') as output_file:
            output_file.write(output_html)
        print(f"HTML file saved to {output_path}")

# Example usage
convert_markdown_with_template("example.md", "template.html")
# Example usage
batch_convert("/path/to/markdown/files")
