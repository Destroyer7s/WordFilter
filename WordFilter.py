import re
import time

def replace_bad_words(data, bad_words):
    count = 0
    op = data
    removed_words = []

    def expand_bad_word_to_include_intentional_misspellings(word):
        chars = list(word)
        op = "[" + "][".join(chars) + "]"
        op = op.replace("[a]", "[a A @]") \
               .replace("[b]", "[b B I3 l3 i3]") \
               .replace("[c]", "(?:[c C \\(]|[k K])") \
               .replace("[d]", "[d D]") \
               .replace("[e]", "[e E 3]") \
               .replace("[f]", "(?:[f F]|[ph pH Ph PH])") \
               .replace("[g]", "[g G 6]") \
               .replace("[h]", "[h H]") \
               .replace("[i]", "[i I l ! 1]") \
               .replace("[j]", "[j J]") \
               .replace("[k]", "(?:[c C \\(]|[k K])") \
               .replace("[l]", "[l L 1 ! i]") \
               .replace("[m]", "[m M]") \
               .replace("[n]", "[n N]") \
               .replace("[o]", "[o O 0]") \
               .replace("[p]", "[p P]") \
               .replace("[q]", "[q Q 9]") \
               .replace("[r]", "[r R]") \
               .replace("[s]", "[s S $ 5]") \
               .replace("[t]", "[t T 7]") \
               .replace("[u]", "[u U v V]") \
               .replace("[v]", "[v V u U]") \
               .replace("[w]", "[w W vv VV]") \
               .replace("[x]", "[x X]") \
               .replace("[y]", "[y Y]") \
               .replace("[z]", "[z Z 2]")
        return op

    for word in bad_words:
        exp_word = expand_bad_word_to_include_intentional_misspellings(word)
        pattern = r'(?P<Pre>\s+)(?P<Word>' + exp_word + r')(?P<Post>\s+|\!\?|\.)'
        matches = re.finditer(pattern, data, flags=re.IGNORECASE)
        for match in matches:
            pre = match.group("Pre")
            post = match.group("Post")
            removed_words.append(match.group("Word"))
            output = pre + '*' * len(word) + post
            op = op.replace(match.group(), output)
            count += 1
            print(f"\rReplaced {count} bad word(s)...", end='', flush=True)
            time.sleep(0.1)  # Add a small delay to simulate live countdown

    with open("removed_words.txt", 'w') as removed_words_file:
        removed_words_file.write("\n".join(removed_words))

    return op, count

def load_bad_words_from_file(file_path):
    try:
        with open(file_path, 'r') as bad_words_file:
            bad_words = [line.strip() for line in bad_words_file if line.strip()]
        return bad_words
    except FileNotFoundError:
        print("Error: Bad words file not found. Please check the file path.")
        return []

def get_user_input():
    file_path = input("Enter the path of the file to filter: ")
    bad_words_file_path = input("Enter the path of the bad words file: ")
    bad_words = load_bad_words_from_file(bad_words_file_path)
    return file_path, bad_words

def main():
    file_path, bad_words = get_user_input()

    try:
        with open(file_path, 'r') as file:
            data = file.read()

        print("Filtering in progress...")

        result, count = replace_bad_words(data, bad_words)

        with open(file_path + "_filtered.txt", 'w') as output_file:
            output_file.write(result)

        print("\nFiltering complete. Filtered data saved to", file_path + "_filtered.txt")
        print("Number of replaced bad words:", count)
        print("Removed words saved to removed_words.txt")

    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")

if __name__ == "__main__":
    main()
