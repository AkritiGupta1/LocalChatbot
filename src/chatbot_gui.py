"""
LocalChatbot GUI - Graphical User Interface
Modern desktop application for file system exploration
"""

import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))
from file_analyzer import FileAnalyzer


class LocalChatbotGUI:
    """GUI Application for LocalChatbot using tkinter."""
    
    def __init__(self, root):
        self.root = root
        self.analyzer = FileAnalyzer()
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        # Window configuration
        self.root.title("LocalChatbot - File System Explorer")
        self.root.geometry("1100x750")
        self.root.minsize(900, 600)
        
        # Main container
        main_container = ttk.Frame(self.root, padding="10")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        main_container.rowconfigure(2, weight=1)
        
        # Header
        self.create_header(main_container)
        
        # Control panel with tabs
        self.create_control_panel(main_container)
        
        # Output area
        self.create_output_area(main_container)
        
        # Footer
        self.create_footer(main_container)
    
    def create_header(self, parent):
        """Create header section."""
        header_frame = ttk.Frame(parent)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        header_frame.columnconfigure(0, weight=1)
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="LocalChatbot - File System Explorer",
            font=("Segoe UI", 14, "bold")
        )
        title_label.grid(row=0, column=0, sticky=tk.W)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Explore files and folders on your system",
            font=("Segoe UI", 10)
        )
        subtitle_label.grid(row=1, column=0, sticky=tk.W)
    
    def create_control_panel(self, parent):
        """Create control panel with tabs."""
        notebook = ttk.Notebook(parent)
        notebook.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Tab 1: File Info
        file_tab = ttk.Frame(notebook, padding="10")
        notebook.add(file_tab, text="📄 File Info")
        self.create_file_info_tab(file_tab)
        
        # Tab 2: Folder Browse
        folder_tab = ttk.Frame(notebook, padding="10")
        notebook.add(folder_tab, text="📁 Folder Browser")
        self.create_folder_tab(folder_tab)
        
        # Tab 3: Read File
        read_tab = ttk.Frame(notebook, padding="10")
        notebook.add(read_tab, text="📖 File Reader")
        self.create_read_file_tab(read_tab)
        
        # Tab 4: Search Files
        search_tab = ttk.Frame(notebook, padding="10")
        notebook.add(search_tab, text="🔍 Search Files")
        self.create_search_tab(search_tab)
    
    def create_file_info_tab(self, parent):
        """Create file information tab."""
        # File path input
        input_frame = ttk.Frame(parent)
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        ttk.Label(input_frame, text="File Path:").grid(row=0, column=0, padx=(0, 5))
        self.file_path_entry = ttk.Entry(input_frame)
        self.file_path_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        browse_btn = ttk.Button(input_frame, text="Browse", 
                               command=lambda: self.browse_file(self.file_path_entry))
        browse_btn.grid(row=0, column=2, padx=(0, 5))
        
        fetch_btn = ttk.Button(input_frame, text="Get File Info", 
                              command=self.fetch_file_info)
        fetch_btn.grid(row=0, column=3)
        
        ttk.Label(parent, text="Note: Enter complete file path and click 'Get File Info'").grid(
            row=1, column=0, sticky=tk.W, pady=(0, 5))
    
    def create_folder_tab(self, parent):
        """Create folder browser tab."""
        input_frame = ttk.Frame(parent)
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        ttk.Label(input_frame, text="Folder Path:").grid(row=0, column=0, padx=(0, 5))
        self.folder_path_entry = ttk.Entry(input_frame)
        self.folder_path_entry.insert(0, os.path.expanduser("~"))
        self.folder_path_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        browse_btn = ttk.Button(input_frame, text="Browse", 
                               command=lambda: self.browse_folder(self.folder_path_entry))
        browse_btn.grid(row=0, column=2, padx=(0, 5))
        
        fetch_btn = ttk.Button(input_frame, text="Browse Folder", 
                              command=self.fetch_folder_contents)
        fetch_btn.grid(row=0, column=3)
        
        # Depth selector
        depth_frame = ttk.LabelFrame(parent, text="Recursion Depth", padding="5")
        depth_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.depth_var = tk.IntVar(value=2)
        for i, depth in enumerate([1, 2, 3]):
            rb = ttk.Radiobutton(depth_frame, text=f"Level {depth}", 
                                variable=self.depth_var, value=depth)
            rb.grid(row=0, column=i, padx=5)
    
    def create_read_file_tab(self, parent):
        """Create file reader tab."""
        input_frame = ttk.Frame(parent)
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        ttk.Label(input_frame, text="File Path:").grid(row=0, column=0, padx=(0, 5))
        self.read_path_entry = ttk.Entry(input_frame)
        self.read_path_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        browse_btn = ttk.Button(input_frame, text="Browse", 
                               command=lambda: self.browse_file(self.read_path_entry))
        browse_btn.grid(row=0, column=2, padx=(0, 5))
        
        read_btn = ttk.Button(input_frame, text="Read File", 
                             command=self.fetch_file_content)
        read_btn.grid(row=0, column=3)
        
        # Lines limit
        lines_frame = ttk.LabelFrame(parent, text="Display Settings", padding="5")
        lines_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(lines_frame, text="Max Lines:").grid(row=0, column=0, padx=(0, 5))
        self.max_lines_var = tk.StringVar(value="50")
        lines_spinbox = ttk.Spinbox(
            lines_frame, from_=10, to=500, textvariable=self.max_lines_var, width=10
        )
        lines_spinbox.grid(row=0, column=1, padx=(0, 20))
    
    def create_search_tab(self, parent):
        """Create search tab."""
        input_frame = ttk.Frame(parent)
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(3, weight=1)
        
        # Directory input
        ttk.Label(input_frame, text="Search in:").grid(row=0, column=0, padx=(0, 5))
        self.search_dir_entry = ttk.Entry(input_frame)
        self.search_dir_entry.insert(0, os.path.expanduser("~"))
        self.search_dir_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        browse_btn = ttk.Button(input_frame, text="Browse", 
                               command=lambda: self.browse_folder(self.search_dir_entry))
        browse_btn.grid(row=0, column=2, padx=(0, 5))
        
        # Pattern input
        ttk.Label(input_frame, text="Pattern:").grid(row=0, column=3, padx=(0, 5))
        self.search_pattern_entry = ttk.Entry(input_frame)
        self.search_pattern_entry.insert(0, "*.txt")
        self.search_pattern_entry.grid(row=0, column=4, sticky=(tk.W, tk.E), padx=(0, 5))
        
        search_btn = ttk.Button(input_frame, text="Search", 
                               command=self.fetch_search_results)
        search_btn.grid(row=0, column=5)
        
        ttk.Label(parent, text="Use wildcards: * (any), ? (single char)").grid(
            row=1, column=0, sticky=tk.W, pady=(0, 5))
    
    def create_output_area(self, parent):
        """Create output display area."""
        output_frame = ttk.LabelFrame(parent, text="Output", padding="5")
        output_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame, height=15, width=80, wrap=tk.WORD,
            font=("Consolas", 10), bg="#ffffff", fg="#2c3e50"
        )
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure tags for styling
        self.output_text.tag_config("success", foreground="#27ae60", font=("Consolas", 10, "bold"))
        self.output_text.tag_config("error", foreground="#e74c3c", font=("Consolas", 10, "bold"))
        self.output_text.tag_config("info", foreground="#3498db", font=("Consolas", 10))
        self.output_text.tag_config("header", foreground="#2c3e50", font=("Consolas", 11, "bold"))
    
    def create_footer(self, parent):
        """Create footer section."""
        footer_frame = ttk.Frame(parent)
        footer_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        footer_frame.columnconfigure(0, weight=1)
        
        clear_btn = ttk.Button(footer_frame, text="Clear Output", command=self.clear_output)
        clear_btn.grid(row=0, column=0, sticky=tk.E, padx=(0, 5))
        
        status_label = tk.Label(
            footer_frame, text="Ready", font=("Segoe UI", 9), fg="#27ae60"
        )
        status_label.grid(row=0, column=1, sticky=tk.W)
        self.status_label = status_label
    
    def browse_file(self, entry_widget):
        """Open file browser dialog."""
        file_path = filedialog.askopenfilename()
        if file_path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, file_path)
    
    def browse_folder(self, entry_widget):
        """Open folder browser dialog."""
        folder_path = filedialog.askdirectory()
        if folder_path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, folder_path)
    
    def fetch_file_info(self):
        """Fetch and display file information."""
        file_path = self.file_path_entry.get().strip()
        
        if not file_path:
            self.display_output("❌ Please enter a file path", "error")
            return
        
        result = self.analyzer.get_file_info(file_path)
        self.display_result(result, "File Information")
    
    def fetch_folder_contents(self):
        """Fetch and display folder contents."""
        folder_path = self.folder_path_entry.get().strip()
        depth = self.depth_var.get()
        
        if not folder_path:
            self.display_output("❌ Please enter a folder path", "error")
            return
        
        result = self.analyzer.get_folder_contents(folder_path, max_depth=depth)
        self.display_result(result, "Folder Contents")
    
    def fetch_file_content(self):
        """Fetch and display file content."""
        file_path = self.read_path_entry.get().strip()
        
        if not file_path:
            self.display_output("❌ Please enter a file path", "error")
            return
        
        try:
            max_lines = int(self.max_lines_var.get())
        except ValueError:
            max_lines = 50
        
        result = self.analyzer.read_file_content(file_path, max_lines)
        self.display_result(result, "File Content")
    
    def fetch_search_results(self):
        """Fetch and display search results."""
        directory = self.search_dir_entry.get().strip()
        pattern = self.search_pattern_entry.get().strip()
        
        if not directory or not pattern:
            self.display_output("❌ Please enter both directory and pattern", "error")
            return
        
        result = self.analyzer.search_files(directory, pattern)
        self.display_result(result, "Search Results")
    
    def display_result(self, result, title):
        """Format and display result."""
        self.clear_output()
        
        if isinstance(result, dict) and "error" in result:
            self.display_output(f"❌ Error: {result['error']}", "error")
        else:
            self.display_output(f"✅ {title}\n" + "="*60, "success")
            self.display_formatted(result)
    
    def display_formatted(self, data, indent=0):
        """Recursively display formatted data."""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    self.display_output(f"\n{'  '*indent}📂 {key}:", "info")
                    self.display_formatted(value, indent + 1)
                else:
                    self.display_output(f"{'  '*indent}  {key}: {value}")
        elif isinstance(data, list):
            for i, item in enumerate(data, 1):
                if isinstance(item, dict):
                    self.display_formatted(item, indent + 1)
                else:
                    self.display_output(f"{'  '*indent}  {i}. {item}")
    
    def display_output(self, text, tag=""):
        """Display text in output area."""
        self.output_text.insert(tk.END, text + "\n", tag)
        self.output_text.see(tk.END)
    
    def clear_output(self):
        """Clear output area."""
        self.output_text.delete(1.0, tk.END)


def main():
    """Main entry point."""
    root = tk.Tk()
    app = LocalChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
