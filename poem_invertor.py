def invert_poem(source_filename: str, dest_filenme: str):
    with open(source_filename, "r", encoding="utf-8") as source_file:
        with open(dest_filenme, "w", encoding="utf-8") as dest_file:
            content = source_file.readlines()
            content_clear = [i.rstrip()[::-1] for i in content]
            content_clear.reverse()
            for line in content_clear:
                dest_file.write(line + "\n")


invert_poem("poem_inverted.txt", "poem_restored.txt")
