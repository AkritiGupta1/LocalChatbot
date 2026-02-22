# LocalChatbot - Quick Start Guide

## Setup Completed ✅

Your LocalChatbot project has been successfully created with **both CLI and GUI versions** and Python 3.13.2 virtual environment!

## Project Structure

```
LocalChatbot/
├── .venv/                   # Virtual environment (auto-created)
├── .vscode/
│   └── tasks.json          # VS Code tasks for running chatbot
├── .github/
│   └── copilot-instructions.md  # Project guidelines
├── src/
│   ├── chatbot.py          # CLI interactive chatbot
│   ├── chatbot_gui.py      # GUI desktop application ⭐ NEW
│   └── file_analyzer.py    # File system analysis module
├── README.md               # Comprehensive documentation
├── QUICKSTART.md           # This guide
├── GUI_GUIDE.md            # GUI documentation
├── requirements.txt        # Python dependencies
└── test_chatbot.py         # Test script for verification
```

## Running the Chatbot

### 🎨 GUI Version (Recommended)

The graphical interface is more user-friendly for most users.

**Option 1: Using VS Code Tasks**
1. Press `Ctrl+Shift+B` in VS Code to see available tasks
2. Select "Run GUI" from the dropdown
3. The desktop application will launch

**Option 2: Using Terminal**
```powershell
cd "C:\Users\Akriti Gupta\OneDrive\Documents\AI Training\LocalChatbot"
python src\chatbot_gui.py
```

### 💻 CLI Version

Classic command-line interface for power users.

**Option 1: Using VS Code Tasks**
1. Press `Ctrl+Shift+B` and select "Run LocalChatbot"
2. The CLI will start in your terminal

**Option 2: Using Terminal**
```powershell
cd "C:\Users\Akriti Gupta\OneDrive\Documents\AI Training\LocalChatbot"
python src\chatbot.py
```

## 🎨 GUI Features

The GUI version provides an intuitive interface with:

### 📄 File Info Tab
- Get detailed file information (size, type, path, dates)
- Browse button to select files graphically
- Instant results display

### 📁 Folder Browser Tab
- Explore folder structures with visual hierarchy
- Adjustable recursion depth (1-3 levels)
- Browse button for easy folder selection
- Shows subdirectories and files with sizes

### 📖 File Reader Tab
- Read file contents directly in the application
- Adjustable line limit (10-500 lines)
- Safe handling of large files (>5MB)
- Displays total lines and line count

### 🔍 Search Files Tab
- Search for files using wildcard patterns (*.txt, *.pdf, etc.)
- Specify search directory
- Results displayed in a scrollable output area
- Support for complex patterns (* and ?)

### 💡 Additional Features
- Tabbed interface for organized workflows
- Color-coded output (green for success, red for errors, blue for info)
- Scrollable output area for large results
- Clear button to reset output
- Real-time result display
- Browse buttons for easy file/folder selection

## 💻 CLI Quick Commands

Once the CLI chatbot is running:

```
>> help                                    # Show all commands
>> file C:\Users\Documents\report.pdf      # Get file details
>> folder C:\Users\Documents               # Browse folder contents
>> read C:\Users\Documents\notes.txt       # Read file contents
>> search C:\Users *.pdf                   # Search for files
>> pwd                                     # Show current directory
>> exit                                    # Exit the chatbot
```

## GUI Workflow Examples

### Example 1: Check File Details
1. Open GUI version
2. Go to "📄 File Info" tab
3. Click "Browse" button or paste file path
4. Click "Get File Info"
5. View detailed information in output area

### Example 2: Browse Your Documents
1. Open GUI version
2. Go to "📁 Folder Browser" tab
3. Enter or browse to `C:\Users\[YourName]\Documents`
4. Set recursion depth to 2
5. Click "Browse Folder"
6. See folder structure with all files and subfolders

### Example 3: Search for All PDFs
1. Open GUI version
2. Go to "🔍 Search Files" tab
3. Set search directory to `C:\Users`
4. Enter pattern: `*.pdf`
5. Click "Search"
6. View all matching files in results

### Example 4: Read a File
1. Open GUI version
2. Go to "📖 File Reader" tab
3. Browse to file (e.g., `config.txt`)
4. Set max lines to 50
5. Click "Read File"
6. View file contents with color-coded output

## What the Chatbot Does

✅ **File Information** - Get detailed info (size, location, type, dates)
✅ **Folder Browsing** - Explore folder structures recursively
✅ **File Reading** - Display file contents safely
✅ **File Search** - Find files matching patterns (wildcards supported)
✅ **Error Handling** - Safe handling of permission errors and invalid paths
✅ **User-Friendly UI** - Modern graphical interface (GUI) or command-line (CLI)

## Troubleshooting

### GUI doesn't start?
1. Check Python version: `python -V`
2. Verify you're in the correct directory
3. Try running the test: `python test_chatbot.py`
4. Check if tkinter is available (should come with Python 3.13)

### File not found error?
- Use absolute file paths
- Check file permissions
- Verify the path exists

### GUI window appears empty?
- Give it a moment to render
- Try clicking on the tabs
- Resize the window to refresh display

### CLI not responding?
- Type `help` for command list
- Check if you're using correct command syntax
- Try the GUI version for visual feedback

## Performance Tips

- **For Large Directory Structures**: Use recursion depth of 1-2 to avoid slowdowns
- **For Many Search Results**: Use specific patterns (e.g., `*.pdf` instead of `*.*`)
- **For Large Files**: Set file reader line limit to 50-100 for faster loading

## Features & Safety

🔒 **Safe File Operations**
- Large files (>5MB) are handled cautiously
- Permission errors are handled gracefully
- Binary files are detected and handled safely

🎯 **User-Friendly**
- Color-coded output with status indicators
- Clear error messages
- Tabbed interface for organized workflows (GUI)
- Help system with command examples (CLI)
- Case-insensitive command input (CLI)

## Next Steps

1. **Start with GUI**: Press Ctrl+Shift+B and select "Run GUI"
2. **Explore Your System**: Use the tabbed interface to browse files
3. **Try Different Features**: Test each tab with various paths
4. **Switch to CLI**: Use the classic CLI for scripting or batch operations
5. **Customize**: Modify source files to add your own features

## Requirements Met ✅

Your chatbot can now:
- Read files on your system
- Tell you where files/folders exist
- Display what files/folders contain
- Search for files by pattern
- Show detailed file information
- Use both GUI and CLI interfaces

---

**Enjoy exploring your file system with LocalChatbot!** 🚀

For more detailed information, see [README.md](README.md) or [GUI_GUIDE.md](GUI_GUIDE.md)
