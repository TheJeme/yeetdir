# Yeetdir

Yeetdir is a command-line application that allows you to convert directories and their contents into JSON format, and vice versa. Yeetdir simplifies the conversion between directories and JSON, providing a flexible and efficient way to manage and interchange directory structure and file contents.

Note: Yeetdir does not support binary files.

# Usage

To convert a directory to JSON:

```sh
yeetdir /path/to/directory
```

To convert JSON to a directory:

```sh
yeetdir /path/to/json-file.json
```

Example .json file:

```json
"root_folder": {
  "subfolder_1": {
    "file_1.go": "This is the content of file 1.",
    "file_2.js": "This is the content of file 2."
  },
  "subfolder_2": {
    "subfolder_3": {
      "file_3.cs": "This is the content of file 3."
    }
  },
  "file_4.py": "This is the content of file 4."
}
```
