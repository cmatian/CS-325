## For Graders - Getting Started
- Unzip the files into a directory on your testing environment.
- This readme assumes you're testing on the flip server which has python built into it (v2.7.5)
- This readme also assumes that you will be reading in your own files for testing. 
Please see below for more information.

### Testing wrestler.py
1) To test the wrestler.py program simply run the following command `python wrestler.py input-file-name`. 
The "input-file-name" should be the name of the file that you want to read into the file. For example, if you have a 
file called `wrestler.txt` that you want to test in the program, simply run the following `python wrestler.py wrestler.txt`

2) The results will be written to the terminal and should look like this:
    ```
    Yes - possible
    Babyfaces: Duke Bear Maxxx 
    Heels: Knight Killer Samson
    ```
3) If the program detects an invalid rivalry pairing (for example, a rivalry is between two heels),
the program will immediately exit with the following message `No - Impossible`.
 
