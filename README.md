# FileScoring
Counts the 10 most used words in each text file in an input folder, and the 10 most used words overall.
Records results to a tiestamped file in a target output folder.
The FileScoringMain.py contains the script.
Takes the following arguments (with default values)
- Input folder path (Input)
- Output path ('')

Functionality details:
- Only .txt files are currently used.
- Words are separated by whitespace characters
- Most punctuuation marks are ignored
- All text is turned to lowercase before processing
