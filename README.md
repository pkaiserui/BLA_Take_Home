# Barren Land Analysis


## Problem Requirements
You have a farm of 400m by 600m where coordinates of the field are from (0, 0) to (399, 599). A portion of the farm is barren, and all the barren land is in the form of rectangles. Due to these rectangles of barren land, the remaining area of fertile land is in no particular shape. An area of fertile land is defined as the largest area of land that is not covered by any of the rectangles of barren land. 

Read input from STDIN. Print output to STDOUT 

Input 

You are given a set of rectangles that contain the barren land. These rectangles are defined in a string, which consists of four integers separated by single spaces, with no additional spaces in the string. The first two integers are the coordinates of the bottom left corner in the given rectangle, and the last two integers are the coordinates of the top right corner. 

Output 

Output all the fertile land area in square meters, sorted from the smallest area to greatest, separated by a space. 

## Sample Input
Sample Input  
{“0 292 399 307”} --- 116800 116800  
Sample Output  
{“48 192 351 207”, “48 392 351 407”, “120 52 135 547”, “260 52 275 547”} --- 22816 192608  

### Installation requirements:  
Install the following to run:  
* Python 3
* Matplotlib
* Numpy

### How to run
cd into the directory with the files  
then run with python main.py and follow the prompts


## Problem-Solving Process

This problem reminded me of an island search algorithm. After reviewing the problem, I thought a BFS would work, but with python there is a limit to the number of recursive callbacks that can be done, so implementing it iteratively was the way I went.

### Breadth-First Search
1. Create a 2d array with all the values being 0
2. Convert the coordinates into an array
3. Populate the array using the coordinates to make the land barren -1
4. Iterate thru each space of land looking for a 0
    1. Add that coordinate to a queue
    2. While the queue is not empty, take the most recent spot and if it is a 0 add 1 to the total amount of land. Change the value to 1 meaning it has been visited
    3. Add the neighbors if they are in bounds, and it is a 0 to the queue
    4. Continue this until the queue is empty
5. After the BFS is finished the loop will continue again looking for a new space that is 0
6. After every spot has been searched return all the different sized fertile areas 
    

Space Complexity: O(m\*n)

Time Complexity: O(m\*n)

To see a live link check out - https://repl.it/@pkaiserui/BLATakeHome

