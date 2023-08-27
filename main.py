import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num1', type=int)
    parser.add_argument('num2', type=int)
    
    args = parser.parse_args()
    result = args.num1 + args.num2
    print(f"The Sum of {args.num1} and {args.num2} is {result}")

if __name__ == "__main__":
    main()
