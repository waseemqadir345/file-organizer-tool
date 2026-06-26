# 📁 File Organizer & Batch Renamer

A Python automation tool that **organizes hundreds of messy files in seconds**.
It sorts files into folders by type, batch-renames them with custom rules, and removes duplicate files automatically.

> Cleaned up a client's downloads folder with **500+ mixed files** in one command.

---

## ✨ Features

- ✅ Sorts files into folders by type (Images, Documents, Videos, etc.)
- ✅ Batch-renames files with custom names (Photo_001, Photo_002...)
- ✅ Detects & removes duplicate files (using file hashing)
- ✅ Handles hundreds of files instantly
- ✅ Uses only Python standard library (no extra installs)

---

## 🛠️ Tech Stack

- **Python 3** (standard library only)
- `os`, `shutil` – file operations
- `hashlib` – duplicate detection
- `argparse` – command-line options

---

## 🚀 Installation

```bash
# 1. Clone the repo
git clone https://github.com/waseemqadir345/file-organizer-tool.git
cd file-organizer-tool

# 2. No dependencies needed - ready to run!
```

📖 Usage
Sort files by type:

python file_organizer.py /path/to/folder


Batch rename files:

python file_organizer.py /path/to/folder --rename Photo


Remove duplicate files:

python file_organizer.py /path/to/folder --dedupe


📂 Project Structure

file-organizer-tool/
├── README.md
├── requirements.txt
├── file_organizer.py
├── .gitignore
└── sample_files/
    └── README.txt


👤 Author
M Waseem Q — Python Developer & Web Automation Specialist
📩 Available for freelance work on Upwork.


📝 License
MIT License — free to use and modify.
