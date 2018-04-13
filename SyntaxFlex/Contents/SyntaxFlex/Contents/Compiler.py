from Translate_ import *

syntax_type = ""

if syntax_type == "":
    syntax_type = raw_input("Syntax: ")

def get_file(file_name):
    file_ = open(file_name, "r")
    final_ = []
    for line in file_:
        final_.append(syntax_changer(line, syntax_type))
    return("\n".join(final_))
    
def compiler():
    try:
        user_input = raw_input(syntax_type + ": ")
        if user_input.split()[0] == "$run":
            data = get_file(user_input.split()[1])
            print(data)
        elif user_input == "$exit":
            return("exit_compiler")
        else:
            data = syntax_changer(user_input, syntax_type)
            print(data)      
    except:
        print("Sorry, if you get this that means that we encountered a bug. We are in beta, so please report this and tell us! Thanks!") 
    
while 0 == 0:
    input_ = compiler()
    if input_ == "exit_compiler":
        break