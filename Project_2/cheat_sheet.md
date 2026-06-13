# Password Generator & Vault: Concepts & Logic Cheat Sheet

This document explains the core programming concepts and the step-by-step logic required to build a Password Generator and Storage Vault, without giving you the actual code.

## 1. Core Programming Concepts

### Randomization and String Constants
To build a secure password, a computer needs to be unpredictable.
* **The `random` module:** Python has built-in tools to pick items randomly from a sequence. This is the engine of your password generator.
* **The `string` module:** Instead of manually typing out "abcdefg..." or "!@#$%", Python has pre-defined constants for all lowercase letters, uppercase letters, digits, and punctuation marks. 
* **String Concatenation & Joining:** You will need to "glue" different character sets together to form a pool of allowed characters, and later glue the randomly picked characters together to form the final password string.

### Data Structures (Dictionaries)
* **Dictionaries:** When saving a password, you need to know what it belongs to. A dictionary is perfect here. You can map a key (like the website name or username) to a value (the generated password).

### Data Serialization (JSON)
* Just like a task manager, a password vault is useless if it forgets your passwords when you close the program. 
* **JSON (JavaScript Object Notation):** We use JSON to translate our Python dictionary of saved passwords into a text format that can be written to a `.json` file securely on your hard drive, and read back into Python memory the next time you open the app.

### Control Flow & Input Validation
* **Boolean Logic (True/False):** You will ask the user yes/no questions (e.g., "Include symbols?"). You'll use their answers to set boolean flags (`True` or `False`) that dictate how the password is built.
* **Try/Except Blocks:** If you ask for a password length of "12" and the user types "twelve", the program will crash. You need logic to catch these `ValueError`s and ask again.

---

## 2. Building Up the Logic (Step-by-Step)

If you were to build this from scratch, here is how you would think through the logic step-by-step:

### Phase 1: The Password Generator Logic
1. **Get Preferences:** Ask the user for their desired password length. Validate that they entered an actual number greater than 0.
2. **Ask for Character Types:** Ask a series of yes/no questions: Include uppercase? Include numbers? Include symbols?
3. **Build the Pool:** Start with a base pool of characters (usually lowercase letters). Check the answers from step 2. If they said yes to uppercase, add the uppercase string to your pool. Repeat for numbers and symbols.
4. **Generate:** Create an empty result. Loop exactly as many times as the desired password length. In each loop, randomly pick *one* character from your pool and add it to the result.
5. **Return:** Send the final generated string back to the user.

### Phase 2: The Vault (Storage) Logic
1. **Setup/Load:** When the program starts, check if a `vault.json` file exists. If it does, read it and convert it into a Python dictionary. If it doesn't, create an empty dictionary.
2. **Saving an Entry:** After a password is generated, ask the user if they want to save it. If yes, ask for the Website/App name and the Username. Add these as a new entry into your loaded dictionary.
3. **Write to Disk:** Immediately overwrite the `vault.json` file with the newly updated dictionary.
4. **Retrieving an Entry:** Create logic that asks the user for a Website name, checks if that name exists as a key in the dictionary, and if so, prints the associated username and password.

### Phase 3: The Interactive Menu
1. Create a `while True` loop to act as the main menu.
2. Present the user with options: 
   * `1.` Generate a New Password
   * `2.` Look up a Saved Password
   * `3.` Exit
3. **Route the user:** 
   * If `1`, trigger the Generator Logic. Then immediately transition into the Saving Logic.
   * If `2`, trigger the Retrieving Logic.
   * If `3`, break the loop to exit.

---

## 3. Useful Tools to Research
* **`random.choice()` vs `random.choices()`:** Look up the difference between these two. One picks a single item, one can pick multiple items at once.
* **List Comprehensions:** A more advanced, cleaner way to write a `for` loop in a single line, highly useful for generating the password string quickly.
* **`str.lower()` and `str.strip()`:** Very useful when evaluating user inputs (like " y " or "Yes") to safely convert them into a uniform format before checking them.
