# WordFilter
 Removes potentially unwanted words from a text file



# Word Filter Python Script

## Overview

`WordFilter.py` is a Python script designed to filter out offensive words and phrases from a given text file. The script uses a list of bad words from `badwords.txt` and employs a flexible pattern matching mechanism to identify and replace variations of these words, including intentional misspellings and character substitutions. Additionally, a list of mixed words from `wordlist.txt` can be used for reference.

## Features

- **Dynamic Bad Word Filtering**: The script dynamically identifies bad words from `badwords.txt` and applies filtering to the input text file.

- **Permutation Handling**: It takes into account intentional misspellings and character substitutions, ensuring that variations of bad words are appropriately filtered.

- **Live Countdown**: During the filtering process, the script provides a live countdown, indicating the number of replaced bad words.

- **Removed Words Tracking**: The script generates a file named `removed_words.txt`, which contains a list of all words that were removed during the filtering process.

## Usage

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Destroyer7s/WordFilter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd WordFilter
   ```

### Running the Script

1. Open a terminal in the project directory.

2. Run the script:

   ```bash
   python WordFilter.py
   ```

3. Follow the prompts to enter the path of the file to filter, the path of the file containing bad words (`badwords.txt`), and the path of the file containing good words (`wordlist.txt`).

4. The script will perform the filtering and provide information on the progress, the number of replaced bad words, and the words that were removed.

### Example

```bash
Enter the path of the file to filter: wordlist.txt
Enter the path of the bad words file: badwords.txt
Filtering in progress...
Replaced 274 bad word(s)...
Filtering complete. Filtered data saved to goodwords.txt_filtered.txt
Number of replaced bad words: 274
Removed words saved to removed_words.txt
```

## Customization

- **Bad Words List**: Update the `badwords.txt` file with the list of bad words. Each line can contain spaces, and phrases are supported.

- **Good Words List**: Update the `wordlist.txt` file with the list of good words. Each line can contain spaces.

- **Delay in Live Countdown**: You can adjust the delay in the live countdown by modifying the `time.sleep` value in the script.
