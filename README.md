#Prolog 
Here is a Python program that reads a collection of files and prints the N words with the maximum occurrences throughout all files.

## Input
Reads from the command line arguments the following:
1. An integer representing how many maximum occurred words to print.
2. A list of paths that represent the directories or files to traverse. If a path is a directory,
that directory should be traversed recursively to find all nested files (may contain sub-directories as well).

### Program​ ​input​ ​example: ​
```
 $ max-words 5 /tmp /home/user/file.txt
```

### Output:
The​ ​N​ ​words​ ​that​ ​have​ ​the​ ​maximal​ ​number​ ​of​ ​occurrences​ ​in​ ​the​ ​following​ ​format:
```
Maximum <N> words:
Word ‘word-1’ occurred ‘x’ times
Word ‘word-2’ occurred ‘y’ times
 … 
Word ‘word-N’ occurred ‘n’ times 
 ```
## Assumptions
1. Was written and tested on windows OS
2. Use python 3.8.0 , and now in order to run the code I use:
```
python.exe C:\Users\nivw2\PycharmProjects\niv\max_words\max_words\cli\max-words.py 3 C:\Windows\Logs\

```
3. root directory must be at C:\\Users\\nivw2\\PycharmProjects\\niv\\max_words , as I still need to solve the
 import path issue.

## List of tasks to finish
* write tests using mock
* read the files in parallel using the multiprocessing Pool
* optimize words data structure during adding words
* fix root import path issue 
