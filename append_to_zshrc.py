#!/usr/bin/env python3

import os
import sys
import shutil

# Path to the .zshrc file
zshrc_path = os.path.expanduser("~/.zshrc")

# Function to append alias to .zshrc
def append_to_zshrc(alias):
    # Check if the alias already exists in .zshrc
    with open(zshrc_path, 'r') as file:
        existing_lines = file.readlines()

    if alias + '\n' not in existing_lines:
        # If alias doesn't exist, append it
        with open(zshrc_path, 'a') as file:
            file.write(alias + '\n')
        print(f"Added: {alias}")
    else:
        print(f"Alias already exists: {alias}")

    print(f"Alias has been added to {zshrc_path}. Please run 'source ~/.zshrc' to apply it.")

# Function to install the script globally
def install():
    # Check if the script is already installed
    install_path = os.path.join(os.path.expanduser("~/.local/bin"), "append_to_zshrc")
    if not os.path.exists(install_path):
        # Get the path of the current script
        current_script = os.path.abspath(__file__)
        
        # Create the target directory if it doesn't exist
        if not os.path.exists(os.path.dirname(install_path)):
            os.makedirs(os.path.dirname(install_path))

        # Copy the script to the install path
        shutil.copy(current_script, install_path)
        os.chmod(install_path, 0o755)  # Make it executable
        print(f"Installed successfully to {install_path}")
    else:
        print("Script is already installed.")

# Main function
def main():
    if len(sys.argv) < 2:
        print("No alias provided. Please pass an alias as an argument.")
        sys.exit(1)

    # Get the alias from the argument
    alias = sys.argv[1]

    # Install or append the alias to .zshrc
    if sys.argv[0] == "install":
        install()
    else:
        append_to_zshrc(alias)

if __name__ == "__main__":
    main()

