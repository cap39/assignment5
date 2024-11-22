import unittest
import os
import subprocess

class LearningCase(unittest.TestCase):
    def test_java_file_exists(self):
        java_file_path = "JavaFiles/ClientGo.java"
        assert os.path.exists(java_file_path), "Java file not found!"

    def test_java_compilation(self):
        java_file_path = "JavaFiles/ClientGo.java"
        result = subprocess.run(["javac", java_file_path], capture_output=True)
        assert result.returncode == 0, f"Compilation failed: {result.stderr.decode()}"
        
    def test_java_output(self):
        java_class_name = "JavaFiles/ClientGo" 
        expected_output = """CarGo Service: Exclusive Mumbai hatchback service for short trips.\r\nCarEATS Service: Mumbai-specific food delivery with top-rated restaurants.\r\nCarGo Service: New Delhi's premium hatchback service.\r\n"""
        result = subprocess.run(["java", java_class_name], capture_output=True)
        assert expected_output in result.stdout.decode(), "Unexpected output from Java program"
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
    


