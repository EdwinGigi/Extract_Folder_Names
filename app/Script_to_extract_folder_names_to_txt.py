import os

def extract_folder_names_to_file(source_folder, output_file):
    # Get all entries in the source folder
    entries = os.listdir(source_folder)
    
    # Filter out files, keeping only directories
    folder_names = [entry for entry in entries if os.path.isdir(os.path.join(source_folder, entry))]
    
    # Sort the folder names alphabetically
    folder_names.sort()
    
    # Write the sorted folder names to the output file
    with open(output_file, 'w') as file:
        for folder_name in folder_names:
            file.write(folder_name + '\n')
            
# Example usage
source_folder = 'C://your/folder/path'  # Update this path to your source folder
output_file = 'C://your/folder/path/output.txt'  # Update this path to your desired output file
extract_folder_names_to_file(source_folder, output_file)

