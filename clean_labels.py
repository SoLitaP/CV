import os

def replace_first_column(file_path):
    """
    Replaces the first column in a text file with '0' and overwrites the source file.

    Parameters:
        file_path (str): Path to the input text file.

    Returns:
        None
    """
    try:
        # Read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Replace the first column in each line with '0'
        updated_lines = []
        for line in lines:
            parts = line.strip().split()  # Split the line into parts
            if parts:  # Check for non-empty lines
                parts[0] = '0'  # Replace the first column with '0'
                updated_lines.append(' '.join(parts))  # Reconstruct the line

        # Overwrite the source file with updated content
        with open(file_path, 'w') as file:
            file.write('\n'.join(updated_lines) + '\n')

        print(f"File '{file_path}' has been successfully updated.")

    except Exception as e:
        print(f"An error occurred: {e}")

DATASET_PATH = os.getcwd() + "\\Dataset\\yoloV5"

TRAIN_PATH = DATASET_PATH + "\\train\\labels"
VALID_PATH = DATASET_PATH + "\\valid\\labels"
TEST_PATH = DATASET_PATH + "\\test\\labels"

for path in [TRAIN_PATH, VALID_PATH, TEST_PATH]:
    for file in os.scandir(path):
        if file.is_file():
            replace_first_column(f"{path}\\{file.name}")