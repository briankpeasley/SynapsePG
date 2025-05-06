import os
import argparse
import json

def convert(name: str, file: str):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
    config = json.load(open(f'{root}/src/utilities/notebook/properties.json', 'r'))

    with open(file, "r") as f:
        lines = f.readlines()

    formatted = []

    in_excluded_region = False
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        if stripped == "#region exclude":
            in_excluded_region = True
            continue
        elif stripped == "#endregion":
            in_excluded_region = False
            continue

        if in_excluded_region:
            continue
        
        formatted.append(stripped + "\r\n")

    config["cells"] = [
            {
                "cell_type": "code",
                "execution_count": 1,
                "source": formatted
            }
        ]
    
    notebook = {
        "name": name,
        "properties": config
    }

    output_file = f"{root}/notebook/{name}.json"
    with open(output_file, "w") as f:
        f.write(json.dumps(notebook, indent=4))

def main():
    parser = argparse.ArgumentParser(description="Convert python script to notebook")
    parser.add_argument("--name", type=str, required=True, help="Name to give the notebook")
    parser.add_argument("--file", type=str, required=True, help="The python script to add to the notebook")

    args = parser.parse_args()
    convert(args.name, args.file)

if __name__ == "__main__":
    main()