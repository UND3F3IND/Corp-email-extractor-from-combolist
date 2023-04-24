import os
import re
import time
import codecs



print(r'''
██    ██ ███    ██ ██████  ██████  ███████ ██████  ██ ███    ██ ██████  
██    ██ ████   ██ ██   ██      ██ ██           ██ ██ ████   ██ ██   ██ 
██    ██ ██ ██  ██ ██   ██  █████  █████    █████  ██ ██ ██  ██ ██   ██ 
██    ██ ██  ██ ██ ██   ██      ██ ██           ██ ██ ██  ██ ██ ██   ██ 
 ██████  ██   ████ ██████  ██████  ██      ██████  ██ ██   ████ ██████  

''')

while True:
    input_file_name = input("Enter the name of the input file: ")
    if not input_file_name:
        print("Input file name cannot be empty. Please try again.")
        continue
    try:
        input_file = codecs.open(input_file_name, "r", encoding="utf-8")
        break
    except FileNotFoundError:
        print(f"File '{input_file_name}' does not exist. Please try again.")

while True:
    output_file_name = input("Enter the name of the output file: ")
    if not output_file_name:
        print("Output file name cannot be empty. Please try again.")
        continue
    if input_file_name == output_file_name:
        print("Input and output file names cannot be the same. Please try again.")
        continue
    if os.path.exists(output_file_name):
        overwrite = input("Output file already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() == 'n':
            continue
        else:
            break
    else:
        break

output_file = codecs.open(output_file_name, "w", encoding="utf-8")

unique_domains = set()

start_time = time.time()

animation = "|/-\\"
i = 0
num_lines_found = 0

for line in input_file:
    parts = line.split(":")
    if len(parts) > 1:
        domain = parts[0].split("@")[-1]
        if domain not in unique_domains:
            unique_domains.add(domain)
            output_file.write(line)
            num_lines_found += 1
    print(f"Processing: {animation[i % len(animation)]} Please wait..", end="\r")
    i += 1

input_file.close()
output_file.close()

time_taken = time.time() - start_time

print(f"Processing: {' ' * len(animation)}", end="\r")

print(f"Lines found: {num_lines_found}")
print(f"Time taken: {time_taken:.2f} seconds")
print(f"Lines saved: {len(unique_domains)}")
