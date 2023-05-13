┊ 𝗨𝗻𝗶𝗾𝘂𝗲 𝗗𝗼𝗺𝗮𝗶𝗻𝘀 𝗘𝘅𝘁𝗿𝗮𝗰𝘁𝗼𝗿 ┊

This script is designed to extract unique domains from an input file and save them in an output file. It helps to identify and collect distinct domain names present in a given dataset.


【Prerequisites】


• Python 3.x

• The following Python modules need to be installed:

   • codecs

   • os

   • re

   • time

【Usage】


1- Run the script using Python: python unique_domains_extractor.py

2- The script will display a ASCII art logo to start with.

3- Enter the name of the input file when prompted. The input file should be a text file containing email addresses or domain names, with each entry on a new line.

4- If the entered input file does not exist, an error message will be displayed, and you will be prompted to enter the input file name again.

5- After successfully providing the input file name, you will be asked to enter the name of the output file.

6- If the entered output file name already exists, you will be prompted to confirm whether you want to overwrite it. If you choose not to overwrite, you can enter a new output file name.

7- Once a valid output file name is provided, the script will process the input file and extract unique domains.

8- During the processing, an animation will be displayed to indicate progress.

9- After completion, the script will display the following information:

   • Number of lines found in the input file that contained domain names.

   • Time taken to process the input file.

   • Number of unique domains saved in the output file.

10- The output file will be saved with the extracted unique domains.

Note: The input file and output file should be provided with their respective extensions, such as .txt.


【Disclaimer】

This script is provided as-is without any warranty. It is the responsibility of the user to ensure the input file is formatted correctly and to handle any errors or exceptions that may arise during the execution of the script.

Please use this script responsibly and in compliance with any relevant laws or regulations.
