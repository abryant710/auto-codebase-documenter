import os
import subprocess


def format_file(file_path):
    subprocess.run(["black", file_path], check=True)


def main():
    for root, dirs, files in os.walk("."):
        if "venv" in dirs:
            dirs.remove("venv")  # don't visit this directory

        for name in files:
            if name.endswith(".py"):
                format_file(os.path.join(root, name))


if __name__ == "__main__":
    main()
