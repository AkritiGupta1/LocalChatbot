"""
File System Analyzer Module
Handles reading and analyzing files on the local system.
"""

import os
from pathlib import Path


class FileAnalyzer:
    """Analyzes files and directories on the local system."""
    
    @staticmethod
    def get_file_info(file_path):
        """
        Get detailed information about a file.
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            dict: File information including size, location, and type
        """
        try:
            path = Path(file_path)
            
            if not path.exists():
                return {"error": f"File not found: {file_path}"}
            
            file_stats = path.stat()
            
            return {
                "name": path.name,
                "full_path": str(path.absolute()),
                "size": file_stats.st_size,
                "size_mb": f"{file_stats.st_size / (1024 * 1024):.2f}",
                "type": path.suffix if path.suffix else "No extension",
                "is_file": path.is_file(),
                "is_directory": path.is_dir(),
                "created": str(path.stat().st_ctime),
                "modified": str(path.stat().st_mtime)
            }
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def get_folder_contents(folder_path, max_depth=2, current_depth=0):
        """
        Get contents of a folder recursively.
        
        Args:
            folder_path (str): Path to the folder
            max_depth (int): Maximum recursion depth
            current_depth (int): Current recursion depth
            
        Returns:
            dict: Folder structure and contents
        """
        try:
            path = Path(folder_path)
            
            if not path.exists():
                return {"error": f"Folder not found: {folder_path}"}
            
            if not path.is_dir():
                return {"error": f"Not a directory: {folder_path}"}
            
            contents = {
                "name": path.name,
                "path": str(path.absolute()),
                "files": [],
                "folders": []
            }
            
            items = sorted(path.iterdir())
            
            for item in items:
                try:
                    if item.is_file():
                        contents["files"].append({
                            "name": item.name,
                            "size": f"{item.stat().st_size / 1024:.2f} KB",
                            "path": str(item.absolute())
                        })
                    elif item.is_dir() and current_depth < max_depth:
                        subfolder = FileAnalyzer.get_folder_contents(
                            item, max_depth, current_depth + 1
                        )
                        contents["folders"].append(subfolder)
                except (PermissionError, OSError):
                    continue
            
            return contents
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def read_file_content(file_path, max_lines=50):
        """
        Read and return file content (limited for large files).
        
        Args:
            file_path (str): Path to the file
            max_lines (int): Maximum number of lines to read
            
        Returns:
            dict: File content and metadata
        """
        try:
            path = Path(file_path)
            
            if not path.exists():
                return {"error": f"File not found: {file_path}"}
            
            if not path.is_file():
                return {"error": f"Not a file: {file_path}"}
            
            # Check file size
            file_size = path.stat().st_size
            if file_size > 5 * 1024 * 1024:  # 5MB
                return {
                    "error": "File too large to display",
                    "file_size": f"{file_size / (1024 * 1024):.2f} MB"
                }
            
            # Try to read as text
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()[:max_lines]
                    content = ''.join(lines)
                    return {
                        "file": path.name,
                        "path": str(path.absolute()),
                        "content": content,
                        "total_lines": len(open(file_path).readlines()),
                        "displayed_lines": len(lines)
                    }
            except UnicodeDecodeError:
                return {
                    "error": "Cannot read file (binary or unsupported encoding)",
                    "file": path.name,
                    "path": str(path.absolute())
                }
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def search_files(directory, pattern):
        """
        Search for files matching a pattern.
        
        Args:
            directory (str): Directory to search in
            pattern (str): File name pattern
            
        Returns:
            list: List of matching files
        """
        try:
            path = Path(directory)
            
            if not path.exists() or not path.is_dir():
                return {"error": f"Invalid directory: {directory}"}
            
            matches = []
            for item in path.rglob(pattern):
                if item.is_file():
                    matches.append(str(item.absolute()))
            
            return {
                "pattern": pattern,
                "directory": str(path.absolute()),
                "matches": matches,
                "count": len(matches)
            }
        except Exception as e:
            return {"error": str(e)}
