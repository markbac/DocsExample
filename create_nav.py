import os
import yaml

def generate_nav(directory, base_path=""):
    """
    Recursively generates a navigation structure for a directory.
    """
    nav = []
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):  # If it's a directory
            sub_nav = generate_nav(item_path, base_path=os.path.join(base_path, item))
            if sub_nav:
                # Replace underscores with spaces in the directory name
                nav.append({item.replace("_", " "): sub_nav})
        elif item.endswith('.md'):  # If it's a Markdown file
            # Replace underscores with spaces in the file name (without extension)
            nav.append({item[:-3].replace("_", " "): os.path.join(base_path, item)})
    return nav

def save_nav_to_file(nav, output_file):
    """
    Saves the generated navigation to a YAML file.
    """
    with open(output_file, 'w') as f:
        yaml.dump(nav, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    # Change 'docs' to the root directory of your documentation files
    docs_directory = "docs"
    output_file = "nav.yml"
    
    navigation = generate_nav(docs_directory)
    save_nav_to_file(navigation, output_file)
    print(f"Navigation file saved to {output_file}")
