import markdown

def convert_markdown_to_html(file_path, css=None):
    with open(file_path, 'r') as file:
        text = file.read()
        html = markdown.markdown(text)
        if css:
            html = f"<link rel='stylesheet' href='{css}'>\n{html}"
        output_path = file_path.replace('.md', '.html')
        with open(output_path, 'w') as output_file:
            output_file.write(html)
        print(f"HTML file saved to {output_path}")

# Example usage
convert_markdown_to_html("example.md", css="styles.css")
