
def main():
    file_path = 'books/frankenstein.txt'
    with open(file_path, 'r') as f:
        file_contents = f.read()
        # print(file_contents)
        return file_contents


def count_words(contents):
    words = contents.split()
    print(len(words))


def sort_on(dict):
    """to sort dict"""
    return dict["num"]


def count_char(contents):
    """Count the number for each character in the file"""
    char = contents.lower()
    char_dict = {}

    for c in char:
        if c.isalpha():
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1

    # Convert dictionary to a list of dictionaries
    char_list = [{"char": key, "num": value} for key, value in char_dict.items()]

    # Sort the list based on the 'num' key in descending order
    char_list.sort(reverse=True, key=sort_on)

    # Print the sorted list
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")


if __name__ == '__main__':
    given_contents = main()
    count_words(given_contents)
    count_char(given_contents)
