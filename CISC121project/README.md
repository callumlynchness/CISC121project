Algorithm: bubble sort

Tests I performed:

Normal Case
    I inputted a normal array (5, 3, 8, 1)
    It returned 1, 3, 5, 8
    ![Normal array](image-2.png)
    Works!
Already sorted:
    I inputted 1, 2, 3, 4, 5
    It detected no swaps and finished instantly
    ![Already sorted](image-1.png)
    Works!
Reverse order/max number of swaps:
    Inputted 5, 4, 3, 2, 1
    It handled the input, sorting the array
    ![Reverse order](image.png)
    Works!
Duplicates:
    Inputted 4, 2, 2, 4, 1
    It handled equal values correctly
    ![Duplicates](image-2.png)
    Works!
Single element:
    In the "Current Step" text box it states "Please enter at least 2 numbers"
    ![Single element](image-1.png)
    Works!
Empty input:
    States "Please enter at least 2 numbers" in the Current Step text box
    ![Empty input](image.png)
    Works!
Non-integers:
    Inputting 5, a, 3 
    Text box says "Input contains non-integers; please use commas and whole numbers"
    ![Non-integer](image.png)

Why I chose it: I chose Bubble Sort as my algorithm for this project because it’s the first sorting algorithm I learned in high school. I find that it’s the most intuitive sorting algorithm for beginners to understand so I figured that would make it perfect for this project! 

Decomposition: What smaller steps form your chosen algorithm? 
Bubble Sort can be broken down into these smaller steps:
Start with an unsorted list of items (e.g., integers in a Python list).


Repeat the following for each pass through the list:


Compare each pair of adjacent elements.


If the left element is greater than the right element, swap them.


Continue passes until:


Either the list is sorted, or you make a full pass with no swaps, meaning the list is already sorted.

Output the sorted list.

Pattern Recognition: How does it repeatedly reach, compare, or swap values? 
Bubble Sort relies on several repeating patterns:
Repeated comparisons:
 Every pass scans the list from the start to the second–last position, comparing values j and j+1.


Repeated swapping pattern:
 Whenever a pair is out of order, the algorithm performs the exact same operation: swap their positions.


Repeated passes:
 The list is processed repeatedly until no disorder is left.


Pattern of convergence:
 After each full pass, the largest unsorted value “bubbles” to its correct position at the end of the list.
 → This means each pass has one fewer value to worry about.

Abstraction: Which details of the process should be shown to the user and how to show it, and which details should be discarded (i.e., not shown)? 

Details to be shown:
	The list of values
	Which two values are being compared
	Whether a swap occurred
	The completion of a pass through the list
	The final sorted list

What to hide:
	Loop counters
	Memory details (pointer movement)
	

Algorithm Design: How will input → processing → output flow to and from the user? Including the use of the graphical user interface (GUI). 

Input:
	The list of numbers
Processing:
	Outer loops controls number of passes
	Inner loop compares adjacent elements
	Swapping logic
	Early exit condition
GUI:
	Highlight compared elements
	Swap animation
	Pass counter
Output:
	Show the fully sorted list
	Total number of swaps

Flowchart: <img width="705" height="1439" alt="image" src="https://github.com/user-attachments/assets/9066ac9a-52a6-4043-9483-e1c5af2e7126" />


Hugging Face link: https://huggingface.co/spaces/callumarii/CISC121project

Done by Callum Lynch

I used ChatGPT and Copilot to help me with edge cases, troubleshoot errors in my code, fix my syntax errors with gradio and other libraries I wasn't too familiar with, describe the implementation of certain features, and answer questions about why my code wouldn't run...
