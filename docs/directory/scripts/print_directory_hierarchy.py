import os

EXCLUDE_DIRS = {"__pycache__", ".git", ".idea", ".venv", "env", "venv", ".mypy_cache"}

def print_tree(start_path, prefix='', output_lines=None):
    if output_lines is None:
        output_lines = []

    try:
        contents = sorted(
            [item for item in os.listdir(start_path) if item not in EXCLUDE_DIRS]
        )
    except PermissionError:
        return output_lines

    pointers = ['├── '] * (len(contents) - 1) + ['└── ']
    for pointer, name in zip(pointers, contents):
        path = os.path.join(start_path, name)
        output_lines.append(prefix + pointer + name)
        if os.path.isdir(path):
            extension = '│   ' if pointer == '├── ' else '    '
            print_tree(path, prefix + extension, output_lines)

    return output_lines

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(script_dir, "../../../langmodels_project_management"))
    output_file = os.path.abspath(os.path.join(script_dir, "../directory_hierarchy.txt"))

    output_lines = [f"{os.path.basename(project_dir)}"]
    output_lines += print_tree(project_dir)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    print(f"Directory hierarchy saved here: {output_file}")

if __name__ == '__main__':
    main()
