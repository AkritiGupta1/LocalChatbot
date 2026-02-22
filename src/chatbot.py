"""
LocalChatbot - Interactive File System Chatbot
Helps users explore and understand files on their local system.
"""

from file_analyzer import FileAnalyzer
import os


class LocalChatbot:
    """Interactive chatbot for local file system exploration."""
    
    def __init__(self):
        self.analyzer = FileAnalyzer()
        self.commands = {
            "help": self.show_help,
            "file": self.get_file,
            "folder": self.get_folder,
            "read": self.read_file,
            "search": self.search_files,
            "pwd": self.show_current_path,
            "exit": self.exit_chat,
            "quit": self.exit_chat,
        }
    
    def show_help(self):
        """Display available commands."""
        help_text = """
╔════════════════════════════════════════════════════════════════╗
║         LocalChatbot - Available Commands                      ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║ file <path>           - Get detailed information about a file  ║
║ folder <path>         - Show folder contents and structure     ║
║ read <path>           - Read and display file contents         ║
║ search <dir> <pattern> - Search for files matching pattern     ║
║ pwd                   - Show current working directory         ║
║ help                  - Show this help message                 ║
║ exit / quit           - Exit the chatbot                       ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

Examples:
  > file C:\\Users\\Documents\\report.pdf
  > folder C:\\Users\\Documents
  > read C:\\Users\\Documents\\notes.txt
  > search C:\\Users\\Documents *.pdf
        """
        print(help_text)
    
    def get_file(self):
        """Get information about a specific file."""
        file_path = input("Enter file path: ").strip()
        if not file_path:
            print("❌ Please provide a file path.")
            return
        
        result = self.analyzer.get_file_info(file_path)
        self._display_result(result)
    
    def get_folder(self):
        """Get information about folder contents."""
        folder_path = input("Enter folder path: ").strip()
        if not folder_path:
            print("❌ Please provide a folder path.")
            return
        
        result = self.analyzer.get_folder_contents(folder_path)
        self._display_result(result)
    
    def read_file(self):
        """Read and display file contents."""
        file_path = input("Enter file path: ").strip()
        if not file_path:
            print("❌ Please provide a file path.")
            return
        
        max_lines = input("Maximum lines to display (default 50): ").strip()
        try:
            max_lines = int(max_lines) if max_lines else 50
        except ValueError:
            max_lines = 50
        
        result = self.analyzer.read_file_content(file_path, max_lines)
        self._display_result(result)
    
    def search_files(self):
        """Search for files matching a pattern."""
        directory = input("Enter directory path: ").strip()
        pattern = input("Enter file pattern (e.g., *.txt): ").strip()
        
        if not directory or not pattern:
            print("❌ Please provide both directory and pattern.")
            return
        
        result = self.analyzer.search_files(directory, pattern)
        self._display_result(result)
    
    def show_current_path(self):
        """Show current working directory."""
        cwd = os.getcwd()
        print(f"\n📁 Current Directory: {cwd}\n")
    
    def exit_chat(self):
        """Exit the chatbot."""
        print("\n👋 Thank you for using LocalChatbot! Goodbye!\n")
        exit(0)
    
    def _display_result(self, result):
        """Format and display results."""
        if isinstance(result, dict):
            if "error" in result:
                print(f"\n❌ Error: {result['error']}\n")
            else:
                print("\n✅ Result:")
                self._print_dict(result, indent=0)
                print()
        elif isinstance(result, list):
            print(f"\n✅ Found {len(result)} results:")
            for item in result:
                print(f"  • {item}")
            print()
    
    def _print_dict(self, data, indent=0):
        """Recursively print dictionary in a readable format."""
        for key, value in data.items():
            if isinstance(value, dict):
                print("  " * indent + f"📂 {key}:")
                self._print_dict(value, indent + 1)
            elif isinstance(value, list):
                if value:
                    print("  " * indent + f"📋 {key}:")
                    for item in value:
                        if isinstance(item, dict):
                            self._print_dict(item, indent + 1)
                        else:
                            print("  " * (indent + 1) + f"• {item}")
                else:
                    print("  " * indent + f"📋 {key}: (empty)")
            else:
                print("  " * indent + f"  {key}: {value}")
    
    def run(self):
        """Start the interactive chatbot."""
        print("\n" + "="*60)
        print("🤖 Welcome to LocalChatbot!")
        print("="*60)
        print("Type 'help' for available commands or 'exit' to quit.\n")
        
        while True:
            try:
                user_input = input(">> ").strip().lower()
                
                if not user_input:
                    continue
                
                # Parse command
                parts = user_input.split(maxsplit=1)
                command = parts[0]
                
                if command in self.commands:
                    self.commands[command]()
                else:
                    print(f"❌ Unknown command: '{command}'. Type 'help' for available commands.\n")
            
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Goodbye!\n")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}\n")


if __name__ == "__main__":
    chatbot = LocalChatbot()
    chatbot.run()
