## For Graders - Getting Started
- Unzip the files into a directory on your testing environment.
- Ensure that your data.txt file is located within the same directory as the python files. Refer to the structure of the zip archive itself for reference.
- This readme assumes you're testing on the flip server which has python built into it (v2.7.5)

### Testing shopping.py
1) To test the shopping.py program simply run the following command `python shopping.py`.

2) An results will be written to an output file called `results.txt` in the same directory.

3) Do note that if you try to view the output text files using a Windows machine (outside of the school server), the line breaks will not exist and you will
need to view it using a text editor like notepad++ (or any IDE that automatically converts linebreaks using your OS's style). Using `vim merge.txt` on the FLIP server will load it with the proper line breaks. I recommend this method.

4) Each time you run the program, the most recent result will be appended to the text file (if it exists). Otherwise, it will generate a new
text file. The execution time will be noted at the bottom of the result so you know which one was most recent. Either way, the result at the bottom is the most recent result.
