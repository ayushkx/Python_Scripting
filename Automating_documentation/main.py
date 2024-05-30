import re
def identify_comment(code , lang):
    patterns = {
        'python':{
            'single_line': r'#[^\n\r]+',
            'multi_line': r'\'\'\'.*?\'\'\'|\"\"\".*?\"\"\"',
        },
        'c_cpp':{
            'single_line': r'\/\/[^\n\r]+',
            'multi_line': r'/\*.*?\*/',
        },
        'java':{
            'single_line': r'\/\/[^\n\r]+',
            'multi_line': r'/\*.*?\*/',
        },
        'javascript':{
            'single_line': r'\/\/[^\n\r]+',
            'multi_line': r'/\*.*?\*/',
        },
        'go':{
            'single_line': r'\/\/[^\n\r]+',
            'multi_line': r'/\*.*?\*/',
        },
    }

    if lang not in patterns:
        raise ValueError(f"the language {lang} is not supported")

    Single_line_pattern = patterns[lang]['single_line']
    multi_line_pattern = patterns[lang]['multi_line']

    single_line_comment = re.findall(Single_line_pattern , code , re.DOTALL)
    multi_line_comment = re.findall(multi_line_pattern , code , re.DOTALL)

    list_comments = single_line_comment + multi_line_comment
    # comments = ''

    # for i in list_comments:
    #     comments = comments + i + '\n'

    return list_comments

def remove_char(text):
    doc_text=[]
    for i in text:
        doc_text.append(re.sub(r'/\*|\*/|\/\/|\#|\'\'\'|\r?\n','',i))
    return doc_text


source_code = """
# One Python statement in one line, terminated by a newline.
# There is no semicolon at the end of a statement.
>>> x = 1     # Assign 1 to variable x
>>> print(x)  # Print the value of the variable x

int main() {
  // This is the comment and is ignored by the compiler.
  cout << "This line is executed by the compiler." << endl;
  /*
    this
    is
    multiline
    comment
  */
  }

'''
 this is the
 way to write
 multiline comment in python
'''

public static void main( String args[] ) {
      // This is the comment and is ignored by the compiler.
      System.out.println( "This line is executed by the compiler." );
      /*
        this
        is
        multiline
        comment
      */
    }

// This is the comment and is ignored by the compiler.
console.log( "This line is executed by the compiler." );
/*
    this
    is
    multiline
    comment
*/

"""

python_comments = identify_comment(source_code , 'python')
python_comments = remove_char(python_comments)
print(f'comments are :{python_comments}')

# c_cpp_comments = identify_comment(source_code , 'c_cpp')
# print(f'comments are :{c_cpp_comments}')


# java_comments = identify_comment(source_code , 'java')
# print(f'comments are :{java_comments}')

# javascript_comments = identify_comment(source_code , 'javascript')
# print(f'comments are :{javascript_comments}')
