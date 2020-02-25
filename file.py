import sys

if len(sys.argv) != 2:
    print("Usage: file.py filename", file=sys.stderr)
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            comment_split = line.strip().split("#")
            num = comment_split[0]

            if num == "":
                continue  # Ignore irrelevant lines

            x = int(num, 2)
            print(f"{x:08b}: {x:d}")

except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} Not Found")
    sys.exit(2)
