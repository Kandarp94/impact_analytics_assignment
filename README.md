<h1>Impact Aanlytics Assignment</h1>
<h2>Question</h2>
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. You are not allowed to miss classes for four or more consecutive days. Your graduation ceremony is on the last day of the academic year, which is the Nth day.</br>

Your task is to determine the following:
<ol>
<li>The number of ways to attend classes over N days.</li>
<li>The probability that you will miss your graduation ceremony.</li>
</ol>
<h2>Prerequisite</h2>
Python 3 must be installed in your local machine.

<h2>How to run ?</h2>
To run the assignment execute following command:</br></br>

```python3 solutions.py 5 ```</br>
Here 5 can be replaced with desired number of days.

```python solutions.py 5 4 ```</br>
Here the second argument 4 is optional which is the number consecutive days student can miss the class. By default it is 4.


<h2>Approach</h2>
On any given day there could be two possibilties either you attend the classes or you miss the classes. I am generating all possible permutation of attending classes (i.e. 2 ^ No_of_days).

Next I am filtering all permutation which has 4 or more consecutive days of absence.

To compute probability I am simply dividing count of invalid permutation by total permutation.

<h3>Time Complexity:</h3> O(2 ^ N) where N is number of days.
