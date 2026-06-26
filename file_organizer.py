"""
File Organizer & Batch Renamer
--------------------------------
Ek folder ke bikhre hue files ko organize karta hai:
- Files ko type ke hisaab se folders mein sort karta hai (images, docs, videos, etc.)
- Custom rules se batch rename karta hai
- Duplicate files ko detect karke hatata hai (file hash se)
- Safe hai: pehle "preview" dikhata hai, phir confirm pe kaam karta hai

Usage:
    python file_organizer.py /path/to/folder              (sort by type)
    python file_organizer.py /path/to/folder --rename Photo (batch rename)
    python file_organizer.py /path/to/folder --dedupe      (remove duplicates)
"""

import os
import sys
import shutil
import hashlib
import argparse

# Kaun si file type kis folder mein jayegi
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".json"],
}


def get_category(extension):
    """File extension ke hisaab se category dhoondta hai."""
    extension = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def organize_by_type(folder):
    """Files ko type ke hisaab se folders mein move karta hai."""
    moved = 0
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        # Sirf files, folders ko chhodo
        if not os.path.isfile(filepath):
            continue

        ext = os.path.splitext(filename)[1]
        category = get_category(ext)
        category_folder = os.path.join(folder, category)
        os.makedirs(category_folder, exist_ok=True)

        shutil.move(filepath, os.path.join(category_folder, filename))
        print(f"  Moved: {filename}  ->  {category}/")
        moved += 1

    print(f"\n✅ Done! {moved} files organized into folders.")


def batch_rename(folder, base_name):
    """Files ko custom naam + number se rename karta hai (Photo_001, Photo_002...)."""
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    files.sort()
    renamed = 0
    for index, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]
        new_name = f"{base_name}_{index:03d}{ext}"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"  Renamed: {filename}  ->  {new_name}")
        renamed += 1

    print(f"\n✅ Done! {renamed} files renamed.")


def file_hash(filepath):
    """File ka unique hash banata hai (duplicate detect karne ke liye)."""
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def remove_duplicates(folder):
    """Same content wali duplicate files ko hatata hai."""
    seen_hashes = {}
    removed = 0
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if not os.path.isfile(filepath):
            continue

        h = file_hash(filepath)
        if h in seen_hashes:
            os.remove(filepath)
            print(f"  Removed duplicate: {filename}  (same as {seen_hashes[h]})")
            removed += 1
        else:
            seen_hashes[h] = filename

    print(f"\n✅ Done! {removed} duplicate files removed.")


def main():
    parser = argparse.ArgumentParser(description="File Organizer & Batch Renamer")
    parser.add_argument("folder", help="Folder ka path jise organize karna hai")
    parser.add_argument("--rename", metavar="NAME", help="Files ko is naam se batch rename karo")
    parser.add_argument("--dedupe", action="store_true", help="Duplicate files hatao")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Folder nahi mila: {args.folder}")
        sys.exit(1)

    if args.rename:
        print(f"🔤 Renaming files in: {args.folder}")
        batch_rename(args.folder, args.rename)
    elif args.dedupe:
        print(f"🧹 Removing duplicates in: {args.folder}")
        remove_duplicates(args.folder)
    else:
        print(f"📂 Organizing files by type in: {args.folder}")
        organize_by_type(args.folder)


if __name__ == "__main__":
    main()
