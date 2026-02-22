# LocalChatbot

An interactive Python chatbot for exploring and analyzing files on your local system. Choose between a modern **graphical interface (GUI)** or a classic **command-line interface (CLI)**.

## Features

- **Two Interfaces**: Modern GUI (tkinter) and Command-Line Interface
- **File Information**: Get detailed information about any file (size, location, type, dates, etc.)
- **Folder Exploration**: Browse folder contents with recursive structure display
- **File Reading**: Read and display file contents (with safety limits)
- **File Search**: Search for files matching specific patterns (wildcards)
- **User-Friendly**: Interactive graphical windows and command-line interface

## Project Structure

```
LocalChatbot/
├── src/CLI chatbot application
│   ├── chatbot_gui.py       # GUI application (tkinter) ⭐ NEW
│   └── file_analyzer.py     # File system analysis module
├── README.md                # This file
├── QUICKSTART.md            # Quick start guide
├── GUI_GUIDE.md             # Comprehensive GUI documentationem analysis module
├── README.md                # This file
├── requirements.txt         # Python dependencies
└── .github/
    └── copilot-instructions.md  # Project guidelines
```

## Prerequisites

- Python 3.8 or higher
- Windows, macOS, or Linux

## Installation

1. Clone or download the project
2. Navigate to the project directory:
   ```bash
   cd LocalChatbot
   ```
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 🎨 GUI Version (Recommended for most users)

Launch the graphical interface:

```bash
python src/chatbot_gui.py
```

**Features:**
- Tabbed interface for organized workflows
- File browser dialogs for easy file/folder selection
- Color-coded output
- Intuitive point-and-click navigation

See [GUI_GUIDE.md](GUI_GUIDE.md) for detailed GUI documentation.

### 💻 CLI Version (For power users and scripting)

Launch the command-line interface:

```bash
python src/chatbot.py
```

Run the chatbot from the `src` directory:

```bash
python chatbot.py
```

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `file <path>` | Get file details | `file C:\Users\Documents\report.pdf` |
| `folder <path>` | Show folder contents | `folder C:\Users\Documents` |
| `read <path>` | Read file contents | `read C:\Users\Documents\notes.txt` |
| `search <dir> <pattern>` | Search files | `search C:\Users\Documents *.pdf` |
| `pwd` | Show current directory | `pwd` |
| `help` | Show help message | `help` |
| `exit` / `quit` | Exit chatbot | `exit` |

## Examples

### Get File Information
```
>> file C:\Users\Documents\report.pdf
✅ Result:
  name: report.pdf
  type: .pdf
  size: 2500000
  size_mb: 2.38
  full_path: C:\Users\Documents\report.pdf
```

### Browse Folder Contents
```
>> folder C:\Users\Documents
✅ Result:
  name: Documents
  path: C:\Users\Documents
  📂 files:
    • report.pdf (2.38 MB)
    • notes.txt (1.25 KB)
  📂 folders:
    • Projects (sub-folder)
```

### Read File
```
>> read C:\Users\Documents\notes.txt
✅ Result:
  file: notes.txt
  total_lines: 50
  displayed_lines: 50
  content: [file content displayed here]
```

### Search Files
```
>> search C:\Users\Documents *.pdf
✅ Found 5 results:
  • C:\Users\Documents\report1.pdf
  • C:\Users\Documents\report2.pdf
  ...
```

## Safety Features

- **File Size Limits**: Large files (>5MB) are not read to prevent memory issues
- **Error Handling**: Comprehensive error handling for inaccessible files/folders
- **Permission Checks**: Handles permission errors gracefully
- **Binary File Detection**: Automatically detects and handles binary files

## Development Guidelines

- Follow PEP 8 coding standards
- Add error handling for all file operations
- Keep code modular and maintainable
- Add type hints where applicable

## Troubleshooting

### Command Not Found
- Make sure you typed the command correctly
- Type `help` to see all available commands

### File Not Found
- Check the file path is correct and file exists
- Use absolute paths for better accuracy
- Ensure you have read permissions

### Permission Denied
- Check file/folder permissions
- Run as administrator if needed
- Try accessing a different file

## Future Enhancements

- File statistics and analytics
- Recursive file analysis
- Configuration file support
- Export results to CSV/JSON
- Advanced search with filters

## License

This project is part of AI Training exercises.

## Author

Created as part of AI Training - LocalChatbot Project
