#!/bin/bash

# Ensure the script is executable
chmod +x append_to_zshrc.py

# Install the Python script to ~/.local/bin
INSTALL_PATH="$HOME/.local/bin/append_to_zshrc"

if [ ! -f "$INSTALL_PATH" ]; then
    cp append_to_zshrc.py "$INSTALL_PATH"
    chmod +x "$INSTALL_PATH"
    echo "Installation complete! You can now run 'append_to_zshrc' from any directory."
else
    echo "Script is already installed at $INSTALL_PATH."
fi

