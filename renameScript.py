import os
import sys

INPUT_FOLDER = r"C:\Code\Book"
PREFIX_TO_MATCH = "_"   # matches anything starting with this
PART_TO_REMOVE = PREFIX_TO_MATCH

def process_folder(root_folder):
    renamed = 0
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".pdf") and filename.startswith(PREFIX_TO_MATCH):
                old_path = os.path.join(dirpath, filename)
                new_filename = filename.replace(PART_TO_REMOVE, "", 1)
                new_path = os.path.join(dirpath, new_filename)

                if os.path.exists(new_path):
                    print(f"SKIP (already exists): {new_path}")
                    continue

                os.rename(old_path, new_path)
                print(f"Renamed: {filename}  →  {new_filename}")
                renamed += 1

    print(f"\nDone. {renamed} file(s) renamed.")

if __name__ == "__main__":
    if not os.path.isdir(INPUT_FOLDER):
        print(f"Folder not found: {INPUT_FOLDER}")
        sys.exit(1)
    process_folder(INPUT_FOLDER)  # ← this line was missing!
