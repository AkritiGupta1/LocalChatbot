"""
Test script for LocalChatbot
Tests the file analyzer functionality
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from file_analyzer import FileAnalyzer

def test_chatbot():
    print("=" * 60)
    print("🧪 Testing LocalChatbot Functionality")
    print("=" * 60)
    
    analyzer = FileAnalyzer()
    
    # Test 1: Get current directory info
    print("\n✅ Test 1: Getting current directory information...")
    cwd = os.getcwd()
    result = analyzer.get_folder_contents(cwd, max_depth=1)
    if "error" not in result:
        print(f"   📁 Folder: {result['name']}")
        print(f"   📊 Files: {len(result['files'])}")
        print(f"   📂 Subfolders: {len(result['folders'])}")
    
    # Test 2: Get this test file info
    print("\n✅ Test 2: Getting file information...")
    test_file = os.path.join(os.path.dirname(__file__), "test_chatbot.py")
    if os.path.exists(test_file):
        result = analyzer.get_file_info(test_file)
        if "error" not in result:
            print(f"   📄 File: {result['name']}")
            print(f"   📏 Size: {result['size']} bytes ({result['size_mb']} MB)")
            print(f"   🏷️  Type: {result['type']}")
    
    # Test 3: Read README
    print("\n✅ Test 3: Reading README.md file...")
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        result = analyzer.read_file_content(readme_path, max_lines=10)
        if "error" not in result:
            print(f"   📖 File: {result['file']}")
            print(f"   📝 Total lines: {result['total_lines']}")
            print(f"   ✂️  Displayed first 10 lines")
    
    # Test 4: Search for Python files
    print("\n✅ Test 4: Searching for Python files...")
    result = analyzer.search_files(cwd, "*.py")
    if "error" not in result:
        print(f"   🔍 Found {result['count']} Python files")
        for match in result['matches'][:3]:
            print(f"      • {os.path.basename(match)}")
    
    print("\n" + "=" * 60)
    print("✅ All tests completed successfully!")
    print("=" * 60)
    print("\n🚀 To run the interactive chatbot, execute:")
    print("   cd src")
    print("   python chatbot.py")
    print()

if __name__ == "__main__":
    test_chatbot()
