# Smart Parent-Child Content Filter
# Load bad words from file
def load_bad_words():
    with open("bad_words.txt", "r") as file:
        words = file.read().splitlines()
    return words


# Filter the sentence
def filter_text(text, bad_words):
    words = text.split()
    filtered_words = []
    bad_count = 0

    for word in words:
        if word.lower() in bad_words:
            filtered_words.append("*" * len(word))
            bad_count += 1
        else:
            filtered_words.append(word)

    filtered_sentence = " ".join(filtered_words)
    return filtered_sentence, bad_count


# Calculate safety score
def safety_score(total_words, bad_count):
    safe_words = total_words - bad_count
    score = (safe_words / total_words) * 100
    return round(score, 2)


# Main Program
def main():

    print("===== Smart Guardian Content Filter =====")

    age = int(input("Enter Child Age: "))

    text = input("Enter the sentence to check: ")

    bad_words = load_bad_words()

    filtered_text, bad_count = filter_text(text, bad_words)

    total_words = len(text.split())

    score = safety_score(total_words, bad_count)

    print("\nFiltered Text:")
    print(filtered_text)

    print("\nSafety Score:", score, "%")

    if bad_count > 2:
        print("⚠ Warning: Unsafe content detected")

    if age < 10 and bad_count > 0:
        print("Strict Mode: Content not suitable for small children")


if __name__ == "__main__":
    main()