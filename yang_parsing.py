from yangify import parser

def print_tree(tree, indent=0):
    for key, value in tree.items():
        print('  ' * indent + key)
        if isinstance(value, dict):
            print_tree(value, indent + 1)
        else:
            print('  ' * (indent + 1) + str(value))

def start():
    print('Inside Parsing Yang Model File')
    # Define the path to your YANG model file
    yang_file = 'model.yang'

    # Parse the YANG file
    model = parser.Parser(yang_file)

    # Print the parsed model structure
    print_tree(model)
