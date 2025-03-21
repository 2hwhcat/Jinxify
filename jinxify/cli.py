import sys
from jinxify.parser import preprocess_code
from jinxify.runtime import PrintWrapper

def main():
    if len(sys.argv) < 2:
        print("Usage: jinxify script.jinfy")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            code = f.read()
        
        exec(preprocess_code(code), {'print': PrintWrapper()})
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)