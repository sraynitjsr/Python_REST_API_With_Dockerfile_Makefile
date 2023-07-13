import argparse

def start():
    print("Inside Reading Command Line Arguments")

    # Create the parser
    parser = argparse.ArgumentParser(description='A simple command-line argument parser example.')

    # Add arguments
    parser.add_argument('--my_number', help='An integer number')

    # Parse the arguments
    args = parser.parse_args()

    # Access the values of the arguments
    input_number = args.my_number

    # Print the values
    print(f'Input Data => {input_number}')
