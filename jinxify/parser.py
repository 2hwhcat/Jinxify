import re

def preprocess_code(code: str) -> str:
    """Convert Jinxify syntax to valid Python"""
    code = re.sub(r'//(.*?)$', r'#\1', code, flags=re.MULTILINE)
    
    code = re.sub(
        r'^(\s*)(if|elif|while|for\s+.*?)\s+(.*?)\s+is\s*$',
        r'\1\2 \3:',
        code,
        flags=re.MULTILINE
    )
    code = re.sub(
        r'^(\s*else)\s+is\s*$',
        r'\1:',
        code,
        flags=re.MULTILINE
    )
    
    return code