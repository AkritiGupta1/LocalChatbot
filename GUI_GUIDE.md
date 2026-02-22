# LocalChatbot GUI - User Guide

## Overview

LocalChatbot now includes a modern graphical user interface (GUI) built with Python's tkinter library. This guide shows you how to use all the features of the GUI application.

## Starting the GUI

### Method 1: VS Code Quick Launch
1. Open the workspace in VS Code
2. Press `Ctrl+Shift+B` to open the task launcher
3. Select **"Run GUI"** from the dropdown
4. The application window will open

### Method 2: Terminal Command
```powershell
cd "C:\Users\Akriti Gupta\OneDrive\Documents\AI Training\LocalChatbot"
.\.venv\Scripts\python.exe src\chatbot_gui.py
```

### Method 3: Python Direct Execution
```powershell
& "C:/Users/Akriti Gupta/OneDrive/Documents/AI Training/LocalChatbot/.venv/Scripts/python.exe" src/chatbot_gui.py
```

## GUI Layout

The application window is organized into several sections:

```
┌─────────────────────────────────────────────────────┐
│  🤖 LocalChatbot - File System Explorer             │
│  Explore files and folders on your system           │
├─────────────────────────────────────────────────────┤
│  [📄 File Info | 📁 Folder | 📖 Reader | 🔍 Search]│
│  ┌───────────────────────────────────────────────┐  │
│  │ Tab Content - Input Fields and Buttons        │  │
│  └───────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────┤
│  📋 Output                                          │
│  ┌───────────────────────────────────────────────┐  │
│  │ Results displayed here                        │  │
│  │ (scrollable text area)                        │  │
│  └───────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────┤
│  [Clear Output]                          Ready      │
└─────────────────────────────────────────────────────┘
```

## Tabs and Features

### 1️⃣ File Info Tab (📄)

**Purpose**: Get detailed information about any file on your system

**How to use:**
1. Click the "📄 File Info" tab
2. Enter or browse to a file path:
   - Type the path directly in the "File Path:" field
   - OR click "Browse" button to select a file graphically
3. Click "Get File Info" button
4. Results appear in the output area

**Information Provided:**
- File name
- Full absolute path
- File size (in bytes and MB)
- File type/extension
- Creation timestamp
- Last modified timestamp

**Example Use Cases:**
- Check file size before opening
- Find exact file location
- Verify file type
- Check when file was last modified

---

### 2️⃣ Folder Browser Tab (📁)

**Purpose**: Explore folder structure and contents

**How to use:**
1. Click the "📁 Folder Browser" tab
2. Enter or browse to a folder path:
   - Default: Your home directory
   - Click "Browse" to select a different folder
   - Type path directly
3. Set "Recursion Depth" (how many levels deep to show):
   - **Level 1**: Only direct contents
   - **Level 2**: Contents + subfolder contents (recommended)
   - **Level 3**: 3 levels deep (slower for large folders)
4. Click "Browse Folder" button
5. View the folder structure in output area

**Information Provided:**
- Folder name and path
- List of all files with sizes
- Subfolder names with their contents
- Nested structure visualization

**Example Use Cases:**
- Explore project directory structure
- Find which subfolders contain what
- Get overview of file organization
- Check available space (via file sizes)

**Performance Tips:**
- Use Level 1-2 for large directories to avoid slowdown
- Level 3 is best for small, well-organized folders

---

### 3️⃣ File Reader Tab (📖)

**Purpose**: Read and display file contents in the application

**How to use:**
1. Click the "📖 File Reader" tab
2. Select a file to read:
   - Type the file path in "File Path:" field
   - OR click "Browse" to select visually
3. Adjust "Max Lines" to display (default: 50):
   - For large files: use 50-100 lines
   - For small files: can increase to 200+
   - Minimum: 10, Maximum: 500
4. Click "Read File" button
5. File contents appear in output area

**Information Provided:**
- Filename
- Full file path
- File contents (up to max lines)
- Total line count
- Number of lines displayed

**Safety Features:**
- Files larger than 5MB cannot be read (prevent memory issues)
- Binary files are detected and handled safely
- Unicode decoding errors are handled gracefully

**Example Use Cases:**
- Read configuration files (`.txt`, `.conf`, `.ini`)
- View Python scripts or code files
- Read log files (last X lines)
- Check file contents before opening in editor
- Quick text file preview

**Supported Formats:**
- Text files: `.txt`, `.md`, `.log`, `.csv`, `.json`, `.xml`, etc.
- Code files: `.py`, `.js`, `.cpp`, `.java`, `.html`, `.css`, etc.

**NOT Supported:**
- Binary files: `.exe`, `.dll`, `.so`, `.pdf`, `.docx`, `.xlsx`
- Very large files: > 5MB

---

### 4️⃣ Search Files Tab (🔍)

**Purpose**: Find files matching specific patterns

**How to use:**
1. Click the "🔍 Search Files" tab
2. Set search parameters:
   - **Search in:** Directory to search (default: home directory)
     - Click "Browse" or type path
   - **Pattern:** File name pattern to match (default: `*.txt`)
     - Use wildcards: `*` (any characters), `?` (single character)
3. Click "Search" button
4. All matching files appear in output area with full paths

**Pattern Examples:**
- `*.pdf` - All PDF files
- `*.py` - Python scripts
- `*.txt` - Text files
- `test_*.py` - Files starting with "test_"
- `*.log` - Log files
- `*` - All files (be careful in large directories!)
- `file??.txt` - "file" + 2 characters + ".txt"

**Information Provided:**
- Total number of matches found
- Complete path for each file
- Search directory
- Pattern used

**Example Use Cases:**
- Find all PDFs in a directory
- Locate Python files in project
- Find recent logs
- Search for backup files
- Find all images in a folder

**Performance Tips:**
- Be specific with patterns (e.g., `*.pdf` not `*.*`)
- Avoid searching the entire C: drive with broad patterns
- Results may take a moment for large directory trees

---

## Output Area

The **📋 Output** section displays results from all operations.

**Features:**
- **Color-coded results:**
  - 🟢 **Green** - Success messages
  - 🔴 **Red** - Error messages
  - 🔵 **Blue** - Information and details
- **Scrollable:** Use scrollbar or mouse wheel
- **Clear Button:** Reset output area for new results
- **Auto-scroll:** Automatically scrolls to show new results

## Tips and Tricks

### Browsing Files and Folders
- When using Browse buttons, standard Windows file dialogs appear
- You can navigate using your familiar file browser
- Copy-paste paths from Windows Explorer to input fields

### Working with Long Paths
- The input fields support full Windows paths
- UNC paths work: `\\computer\share\folder`
- Relative paths are supported from current working directory

### Managing Output
- Clear output between operations for cleaner view
- Output is searchable if you enable text selection
- Can't directly copy-paste from output, but can see full results

### Error Handling
- If path doesn't exist: Clear message appears
- If permission denied: Error message shows which folder
- If file too large: Helpful message with file size

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Move between input fields |
| `Enter` | Submit current tab's action (if focused on button) |
| `Ctrl+A` | Select all text in output area |
| `Ctrl+C` | Copy selected text from output |
| `Ctrl+Shift+B` | Quick task launcher (in VS Code) |

## Troubleshooting

### GUI Window Won't Open
**Problem:** Application launches but window doesn't appear
- **Solution:** Check Python version: `.\.venv\Scripts\python.exe -V`
- **Solution:** Try moving window from edge of screen
- **Solution:** Restart the application

### "File not found" Error
**Problem:** Enter path but get error message
- **Solution:** Check path is correct and file exists
- **Solution:** Use absolute paths (C:\Users\...)
- **Solution:** Try Browse button to select visually
- **Solution:** Check file permissions

### Output Area Empty After Search
**Problem:** Search runs but shows no results
- **Solution:** Check pattern syntax (needs `*` or `?`)
- **Solution:** Try broader search pattern
- **Solution:** Verify search directory contains files
- **Solution:** Check if you have permission to access files

### GUI Runs Slowly
**Problem:** Application is sluggish
- **Solution:** Reduce recursion depth in Folder Browser
- **Solution:** Use specific search patterns
- **Solution:** Close other applications
- **Solution:** Reduce file limit in File Reader

### Special Characters in Path
**Problem:** Path with spaces or special characters causes issues
- **Use Browser:** Click Browse button to handle paths automatically
- **Quote Paths:** Enclose in quotes: `"C:\My Documents\file.txt"`

## Performance Guide

### Quick Operations (< 1 second)
- File Info - any file
- File Reader - small files (<1MB)
- Search - specific patterns in small directories

### Medium Operations (1-5 seconds)
- Folder Browser Level 1 - moderate sized folders
- File Reader - medium files (1-5MB)
- Search - broad patterns in moderate directories

### Slow Operations (may take longer)
- Folder Browser Level 3 - large/complex folder structures
- Search - `*.*` in entire C: drive
- Search - in network locations

## Comparison: GUI vs CLI

| Feature | GUI | CLI |
|---------|-----|-----|
| **Ease of Use** | Very Easy | Moderate |
| **Visual Browsing** | Yes | No |
| **Speed** | Good | Very Fast |
| **Batch Operations** | No | Yes |
| **Learning Curve** | Minimal | Minimal |
| **Accessibility** | Modern UI | Text-based |

## Best Practices

1. **Always Use Browse Buttons** for file/folder selection when unsure of path
2. **Start with Small Folders** using recursion depth 1-2
3. **Use Specific Patterns** in search to avoid overwhelming results
4. **Check File Size** with File Info before reading large files
5. **Clear Output** between operations for better clarity

## Advanced Usage

### Network Paths
```
Search in: \\SERVER\SHARE\Documents
Pattern: *.pdf
```

### Slow/Network Drives
- Use Level 1 recursion only
- Use very specific search patterns
- May need to wait longer for results

### Regular Expression Patterns
- Supports basic wildcards: `*` and `?`
- For complex patterns, use the CLI version

## Getting Help

**Within the Application:**
- Use input field labels and hints
- "Note:" text under each tab provides tips
- Output displays clear error messages

**CLI Alternative:**
- Type `help` in the CLI version for command reference
- More advanced options available in CLI

**File System Explorer:**
- For complex file browsing, use Windows Explorer
- Chatbot excels at getting file details quickly

---

**Happy file system exploring!** 🚀

For more information, see [QUICKSTART.md](QUICKSTART.md) or [README.md](README.md)
