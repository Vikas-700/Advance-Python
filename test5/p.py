# List of Python files to be merged
files_to_merge = ['1st.py', '2st.py', '3rd.py','4rt.py','5th.py','6th.py','7th.py','8th.py','9th.py','10th.py']

# Output file where the combined content will be written
output_file = 'merged_output.py'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Loop through each Python file
    for file_name in files_to_merge:
        # Open each Python file in read mode
        with open(file_name, 'r') as infile:
            # Read and write the content of the file to the output file
            outfile.write(infile.read())
            # Optionally, add a newline or a comment to separate the content
            outfile.write("\n\n# --- End of {} ---\n\n".format(file_name))
