import os
import json
import sys

def is_binary_file(file_path):
    with open(file_path, 'rb') as f:
        preview = f.read(1024)
        return b'\x00' in preview

def folder_to_json(path):
  data = {}
  skipped_files = 0
  if os.path.isdir(path):
    for root, dirs, files in os.walk(path):
      current_dir = data
      for dir in dirs:
        current_dir[dir] = {}
        current_dir = current_dir[dir]
      for file in files:
        file_path = os.path.join(root, file)
        if is_binary_file(file_path):
          skipped_files += 1
          continue 
        with open(file_path, 'r') as f:
          file_content = f.read()
        current_dir[file] = file_content
  print(f"Skipped {skipped_files} binary files")
  return json.dumps(data, indent=4)

def json_to_folder(json_data, path):
  data = json.loads(json_data)
  for name, content in data.items():
    full_path = os.path.join(path, name)
    if isinstance(content, dict):
      json_to_folder(json.dumps(content), full_path)
    else:
      os.makedirs(os.path.dirname(full_path), exist_ok=True)
      with open(full_path, 'w+') as f:
        f.write(content)

def main():
  path = sys.argv[1]
  if path.endswith('.json') and os.path.exists(path):
    with open(path, 'r') as file:
      json_data = file.read() 
      output_path = os.path.join(os.path.dirname(path), os.path.basename(path)[:-5])
      json_to_folder(json_data, output_path)
  elif os.path.exists(os.path.dirname(path)):
    json_data = folder_to_json(path)
    with open(f"{path}/{os.path.basename(path)}.json", 'w+') as file:
      file.write(json_data) 

if __name__ == '__main__':
  main()