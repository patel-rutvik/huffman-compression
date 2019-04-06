# Encryped Arduino Communication
## Summary
This program demonstrates the implementation of the "greedy" [Huffman Algorithm](https://en.wikipedia.org/wiki/Huffman_coding "Huffman Algorithm"). To achieve this, we compress each bit using a huffman tree, and also compress the huffman tree itself using the [Pickle Module](https://docs.python.org/3.1/library/pickle.html "Pickle Module"). It is then decompressed by walking up the  tree and displayed on localhost:8000 on the user's computer.
## How To Use
In order to correctly run the program, you must first navigate to the program directory. then use the command:
```bash
python3 ../webserver.py
```
You can then find the default picture visible at [this link](localhost:8000)

The program can also strictly compress a file and create a new output file, simply with a '.huf' extension on it. To compress your file, use the command:
```bash
python3 ../compress.py <file_to_compress_here>
```

You can also view a specific image being compressed/decompressed. Save your file in the wwwroot/ project directory and use the command above. To view the file, visit the web address:
```
localhost:8000/<file_name_here>
```
