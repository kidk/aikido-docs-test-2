import os
import sys
import shutil
import re

def format_name(name):
    # Convert to lowercase and replace spaces with dashes
    return name
    # return name.replace(' ', '-').lower()

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def remove_curly_braces_from_titles(content):
    # Split into lines to process headers only
    lines = content.split('\n')
    processed_lines = []

    for line in lines:
        # Check if line starts with one or more #
        if line.strip().startswith('#'):
            # Remove {...} only from header lines
            line = re.sub(r'\s*{[^}]*}', '', line)
        processed_lines.append(line)

    return '\n'.join(processed_lines)

def remove_first_header(content):
    content = remove_curly_braces_from_titles(content)

    # Split content into lines
    lines = content.split('\n')
    # Find first header line
    for i, line in enumerate(lines):
        if line.strip().startswith('# '):
            # Remove that line and return remaining content
            return '\n'.join(lines[:i] + lines[i+1:])
    # If no header found, return original content
    return content

def process_markdown_files(old_root, content_dir):
    # Create the content directory if it doesn't exist
    ensure_directory_exists(content_dir)

    # Walk through old directory tree
    for current_dir, dirs, files in os.walk(old_root, topdown=False):
        # Calculate the relative path from old_root
        rel_path = os.path.relpath(current_dir, old_root)

        # Create corresponding directory in content_dir
        if rel_path != '.':
            new_dir_path = os.path.join(content_dir, format_name(rel_path))
            ensure_directory_exists(new_dir_path)
        else:
            new_dir_path = content_dir

        # Process files
        for filename in files:
            if filename.endswith('.md'):
                old_file_path = os.path.join(current_dir, filename)
                new_filename = format_name(filename)
                new_file_path = os.path.join(new_dir_path, new_filename)

                # Read the content of the original file
                with open(old_file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Format the title (without .md extension)
                old_title = os.path.splitext(filename)[0]
                title = format_name(old_title)

                # Create new content with title
                content = remove_first_header(content)
                if not content.startswith('---\ntitle:'):
                    new_content = f'---\ntitle: {old_title}\n---\n\n{content}'
                else:
                    new_content = content

                # Write to new location
                with open(new_file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Processed and copied: {old_file_path} -> {new_file_path}")

def main():
    old_directory = "./old"
    content_directory = "./src/content/docs"

    print(f"Processing directory: {old_directory}")
    print(f"Copying to: {content_directory}")
    process_markdown_files(old_directory, content_directory)
    print("Processing complete")

if __name__ == "__main__":
    main()
