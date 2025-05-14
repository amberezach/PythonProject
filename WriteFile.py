with open("Text.txt", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("Text.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)

