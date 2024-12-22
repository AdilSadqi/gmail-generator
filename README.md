# Gmail Alias Generator

This project is a simple Python script that generates email aliases for a specified Gmail account using Arabic names. The aliases are saved to a text file (`emails.txt`) for later use.

---

## Features

- **Easy to Use**: Generate Gmail aliases by simply providing your Gmail account and the desired number of aliases.
- **Customizable**: The list of names used for alias generation can be easily modified.
- **Output to File**: Generated aliases are automatically saved to `emails.txt`.
- **Batch Generation**: Quickly create a large number of email aliases (e.g., 1000+).

---

## Prerequisites

- Python 3.7 or higher.

---

## Usage

1. Save the script as `gmail_generator.py`.
2. Run the script:
   ```bash
   python gmail_generator.py
   ```
3. Follow the prompts:
   - Enter your Gmail account (without `@gmail.com`).
   - Specify the number of email aliases to generate.

4. The generated aliases will be saved to `emails.txt` in the current directory.

---

## Customization

### Modify Arabic Names

You can change the list of names used for alias generation by editing the `arabic_names` list in the script:
```python
arabic_names = [
    "ahmed", "mohammed", "ali", "fatima", "sarah", "omar", "zainab",
    "layla", "noura", "hassan", "yasmine", "khalid", "salma"
    # Add more names as needed
]
```

### Change Output File

By default, the aliases are saved to `emails.txt`. You can modify the `save_to_file` function to change the output file name or location:
```python
def save_to_file(aliases):
    with open("your_custom_file.txt", "w") as file:
        for alias in aliases:
            file.write(alias + "\n")
```

---

## Example

### Input

- Gmail Account: `exampleuser`
- Number of Aliases: `5`

### Output (in `emails.txt`):
```plaintext
exampleuser+ahmed0@gmail.com
exampleuser+mohammed1@gmail.com
exampleuser+ali2@gmail.com
exampleuser+fatima3@gmail.com
exampleuser+sarah4@gmail.com
```

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Author

Created by **ASADQI**

- **Website**: [https://asadqi.com](https://asadqi.com)
- **Contact**: You can reach out via the website for any queries or support.

---

Enjoy using the Gmail Alias Generator!

