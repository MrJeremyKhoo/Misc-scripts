import os
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
current_directory = os.getcwd()
for filename in os.listdir(current_directory):
    if filename.endswith(".yaml"):
        with open(os.path.join(current_directory,filename), "r") as yaml_file:
            yaml_content = yaml_file.read()


        # Convert YAML to Markdown
        markdown_output = yaml_to_markdown(yaml_content)

        #Output file name
        markdown_filename = os.path.splitext(filename)[0] + ".md"

        # Print the resulting Markdown
        with open(os.path.join(current_directory, markdown_filename), "w") as markdown_file:
            markdown_file.write(markdown_output)

