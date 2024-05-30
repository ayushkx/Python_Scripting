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

def generate_markdown(comment):
    markdown_doc = "##Documentation of the following code\n\n"
    for i in comment:
        markdown_doc += f" -{i}\n"

    return markdown_doc


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
lang = input("Please enter the language (python , c_cpp , java , javascript): ")

markdown = ''

if lang == "python" :
    python_comments = identify_comment(source_code , lang)
    python_comments = remove_char(python_comments)
    print(f'comments are :{python_comments}')
    markdown = generate_markdown(python_comments)

elif lang == "c_cpp":
    c_cpp_comments = identify_comment(source_code ,lang)
    c_cpp_comments= remove_char(c_cpp_comments)
    print(f'comments are :{c_cpp_comments}')
    markdown = generate_markdown(c_cpp_comments)

elif lang == "java":
    java_comments = identify_comment(source_code , lang)
    java_comments = remove_char(java_comments)
    print(f'comments are :{java_comments}')
    markdown = generate_markdown(java_comments)

elif lang == "javascript":
    javascript_comments = identify_comment(source_code , lang)
    javascript_comments = remove_char(javascript_comments)
    print(f'comments are :{javascript_comments}')
    markdown = generate_markdown(javascript_comments)

#markdown = generate_markdown(python_comments)

with open("Documentation.md" , 'w') as file:
    file.write(markdown)


# # VOLUME GETTING BACKED UP REPORT
# <hr>
# LANGUAGES AND TECHNOLOGIES USED IN STORAGE VOLUME UTILIZATION
# <hr>
# Listed are all the technologies and languages supported in order to fetch the "volume which are getting backed up" Report.

# Name:
# - Ansible
# - HTML
# - GitHub Action

# HOW IT WILL WORK
# <hr>

# | Name	   |           Compatibility	            |             Description                                                             |
# |---------|-------------------------------------|-------------------------------------------------------------------------------------|
# | Script	 | YAML. Ansible and GitHub action	    |    The ansible playbook will fetch the "volume which are getting backed up" Report  |
# <br>

# #### script will fetch the volume getting backed up from storage servers. Line 2 to 16 - Fetching all volume which are getting backed up details .
# ![image](https://github.com/ExxonMobil/Volumes_backed_up/assets/58135144/20d8a9e3-6d8d-4539-8ee8-63c9b5550207)
# <br>
# <hr>

# #### appending data's in csv file Line 18 to 28 -

# ![image](https://github.com/ExxonMobil/Volumes_backed_up/assets/58135144/89cdfac6-8358-46f3-a45b-d482078073c8)
# <br>
# <hr>

#  #### Once above stpes done the team will get an email with all result files. Email sending part with attachment Line 30 to 52

# ![image](https://github.com/ExxonMobil/Volumes_backed_up/assets/58135144/06296766-2115-4bf8-b225-ae39d7a5f7b8)
