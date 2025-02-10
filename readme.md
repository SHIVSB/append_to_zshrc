# append_to_zshrc

`append_to_zshrc` is a simple Python script that allows you to easily add custom Git aliases (or any other aliases) to your `.zshrc` file. You can install the script globally and use it from anywhere to streamline your Git workflow by adding pre-defined aliases.

## Features

- Add Git aliases (or any custom aliases) to your `.zshrc` file.
- Check if an alias already exists before adding it to avoid duplicates.
- Easy installation using a one-click installer (`install.sh`).
- Global access to the script once installed.

## Prerequisites

- Python 3.x (ensure you have Python 3 installed on your system).
- A Unix-like OS (macOS/Linux). If you're on Windows, you can use WSL (Windows Subsystem for Linux) to run this script.
- A terminal with `zsh` as your shell.

## Installation

To install the `append_to_zshrc` script, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/SHIVSB/append_to_zshrc.git
cd append_to_zshrc
```
### 2. Run the Installer

```bash
bash install.sh
```

```
Usage: append_to_zshrc "alias gc='git commit'"
```
