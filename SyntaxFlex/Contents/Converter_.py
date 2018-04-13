import os

def remove_spaces(data):
    string_ = False
    final_data = []
    for char in data:
        if char == "'":
            if string_ == False:
                string_ = True
            else:
                string_ = False
        if string_ == True:
            if char == " ":
                final_data.append("$space$")
            else:
                final_data.append(char)
        else:
            final_data.append(char)
    return("".join(final_data))
            
def add_spaces(data):
    return(data.replace("$space$", " "))
    
def read_file(file_name):
    directory = os.path.dirname(os.path.abspath(__file__))+"/Packages/"
    fl = open(directory+file_name, "r")
    inp = []
    outp = []
    verify = False
    for line in fl:
        line = line.replace("\n", "").replace(" ", "")
        if line == "$change_to_outp":
            verify = True
        if verify == False:
            inp.append(line)
        else:
            outp.append(line)
    del outp[0]
    #print inp
    #print outp

    return([inp, outp])

def translate(data, inp, outp): 
        for num in range(len(inp)):
            inp[num] = str(num) + "[/]" + inp[num]
            outp[num] = str(num) + "[/]" + outp[num]
        inp = sorted(inp, key=len)
        new_outp = []
        for organize in range(len(inp)):
            id_ = inp[organize].split("[/]")[0]
            inp[organize] = inp[organize].split("[/]")[1]
            for organize2 in range(len(outp)):
                if outp[organize2].split("[/]")[0] == id_:
                    new_outp.append(outp[organize2].split("[/]")[1])
        outp = new_outp
        data_split = data.split()
        new_outp = []
        new_inp = []
        for data in reversed(outp):
            new_outp.append(data)
        for data in reversed(inp):
            new_inp.append(data)
        inp = new_inp
        outp = new_outp
        for num in range(len(data_split)):
            verify = False
            for word in inp:
                if word in data_split[num]:
                    verify = True
                    break
            if verify == True:
                for num1 in range(len(inp)):
                    if inp[num1] in data_split[num]:
                        data_split[num] = data_split[num].replace(inp[num1], outp[num1])
                        break
                    else:
                        continue
            else:
                continue
        return(" ".join(data_split))
def strings(data, inp, outp):
    data = remove_spaces(data.replace('"', "'").replace("'", "_'")) + " None"
    string_data = data.split("_")
    final_data, strings, stringless, string_count = [], [], [], 0
    for string in range(len(string_data)):
        if string_data[string][0] == "'" and string_data[string+1][0] == "'": 
                string_data[string+1] = string_data[string+1][1:]
                string_data[string] = string_data[string] + "'"
    for string in range(len(string_data)):
        if string_data[string][0] == "'":
            strings.append(add_spaces(string_data[string]))
            stringless.append(" $" + str(string_count) +"$ ")
            string_count += 1
        else:
            stringless.append(string_data[string])
    
    final_data = translate("".join(stringless), inp, outp)
    
    for count in range(len(strings)):
        final_data = final_data.replace("$"+str(count)+"$", strings[count])
    
    return(" ".join(final_data.split()[:-1]))
    
def syntax_changer(data, file_name):
    syntax = read_file(file_name + ".cpff")
    inp = syntax[0]
    outp = syntax[1]
    final_data = strings(data, inp, outp)
    return(final_data)