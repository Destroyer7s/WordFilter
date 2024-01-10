# WordFilter
 Removes potentially unwanted words from a text file
Certainly! Here's the README in Markdown format:

```markdown
# Word Filter Python Script

## Overview

This Python script is designed to filter out offensive words and phrases from a given text file. The script uses a list of bad words and employs a flexible pattern matching mechanism to identify and replace variations of these words, including intentional misspellings and character substitutions.

## Features

- **Dynamic Bad Word Filtering**: The script dynamically identifies bad words from a provided list and applies filtering to the input text file.

- **Permutation Handling**: It takes into account intentional misspellings and character substitutions, ensuring that variations of bad words are appropriately filtered.

- **Live Countdown**: During the filtering process, the script provides a live countdown, indicating the number of replaced bad words.

- **Removed Words Tracking**: The script generates a file named `removed_words.txt`, which contains a list of all words that were removed during the filtering process.

## Usage

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/word-filter-python-script.git
   ```

2. Navigate to the project directory:

   ```bash
   cd word-filter-python-script
   ```

### Running the Script

1. Open a terminal in the project directory.

2. Run the script:

   ```bash
   python word_filter.py
   ```

3. Follow the prompts to enter the path of the file to filter and the path of the file containing bad words.

4. The script will perform the filtering and provide information on the progress, the number of replaced bad words, and the words that were removed.

### Example

```bash
Enter the path of the file to filter: input.txt
Enter the path of the bad words file: bad_words.txt
Filtering in progress...
Replaced 3 bad word(s)...
Filtering complete. Filtered data saved to input_filtered.txt
Number of replaced bad words: 3
Removed words saved to removed_words.txt
```

## Customization

- **Bad Words List**: Create a text file containing the list of bad words. Each line can contain spaces, and phrases are supported.

- **Delay in Live Countdown**: You can adjust the delay in the live countdown by modifying the `time.sleep` value in the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The script utilizes regular expressions and string manipulation techniques.
- Special thanks to OpenAI for providing language models that assist in creating powerful and versatile scripts.
```

Feel free to use and modify this Markdown template as needed.
