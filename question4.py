import unittest
import os
import subprocess

class LearningCase(unittest.TestCase):
    def test_java_file_exists(self):
        java_file_path = "JavaFiles/ClientPayment.java"
        assert os.path.exists(java_file_path), "Java file not found!"

    def test_java_compilation(self):
        java_file_path = "JavaFiles/ClientPayment.java"
        result = subprocess.run(["javac", java_file_path], capture_output=True)
        assert result.returncode == 0, f"Compilation failed: {result.stderr.decode()}"
        
    def test_java_output(self):
        java_class_name = "JavaFiles/ClientPayment" 
        expected_output = "Validation successful.\r\nLogging payment request...\r\nCard Number: 1234567812345678\r\nAmount: $150.0\r\nProcessing payment with PayPal...\r\nCard Number: 1234567812345678\r\nAmount: $150.0\r\nInvalid card number.\r\n"
        result = subprocess.run(["java", java_class_name], capture_output=True)
        assert expected_output in result.stdout.decode(), "Unexpected output from Java program"
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
    


