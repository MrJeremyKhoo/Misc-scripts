import os
import yaml
import json
from collections import Counter

# Directory containing YAML files
yaml_directory = os.getcwd()

# Initialize a Counter to keep track of tag counts
tag_counter = Counter()

# Iterate through each YAML file in the directory
for filename in os.listdir(yaml_directory):
    if filename.endswith('.yaml'):
        yaml_path = os.path.join(yaml_directory, filename)
        with open(yaml_path, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
            tags = data.get('tags', [])
            tag_counter.update(tags)

# Convert the Counter to a dictionary
tag_counts = dict(tag_counter)

# Save the tag counts as JSON
json_output_path = 'tag_counts.json'
with open(json_output_path, 'w') as json_file:
    json.dump(tag_counts, json_file, indent=4)

print(f"Tag counts saved to {json_output_path}")
