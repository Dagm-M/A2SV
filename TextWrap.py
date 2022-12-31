import textwrap

def wrap(string, max_width):
    newString = []
    for index in range(len(string)):
        newString.append(string[index])
        if (index + 1) % max_width == 0:
            newString.append("\n")
            
    return "".join(newString)

if __name__ == '__main__':
