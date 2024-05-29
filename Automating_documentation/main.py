import re
def identify_comment(code , lang):
    patterns = {
        'python':{
            'single_line': r'#.*',
            'multi_line': r'\'\'\'.*?\'\'\'|\"\"\".*?\"\"\"',
        }
    }