import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [name]")
    sys.exit()

print('hi', sys.argv[1])
