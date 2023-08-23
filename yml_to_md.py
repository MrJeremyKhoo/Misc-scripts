import yaml

def yaml_to_markdown(yaml_content):
    markdown = ""
    
    # Parse the YAML content
    yaml_data = yaml.safe_load(yaml_content)
    
    # Convert YAML data to Markdown
    for key, value in yaml_data.items():
        markdown += f"## {key}\n\n{value}\n\n"

    return markdown

# Read YAML content from the file
with open("input.yaml", "r") as yaml_file:
    yaml_content = yaml_file.read()


# Convert YAML to Markdown
markdown_output = yaml_to_markdown(yaml_content)

# Print the resulting Markdown
with open("output.md", "w") as markdown_file:
    markdown_file.write(markdown_output)

