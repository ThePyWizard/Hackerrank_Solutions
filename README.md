# Here is my HackerRank Solutions

>The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.




## Solution Approach

>In the "Solution Approach" section, provide a detailed explanation of your approach to solving the problem. Describe the algorithm, data structures, and any key insights that led to your solution. This helps others understand your thought process and learn from your solutions.

## 1. A Very Big Sum

  - [Problem](https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](averybigsum.py) (navigate to the Solution file)
  - Explanation:
  >This problem  takes an integer as length of the array and array input and then calculates long int sum of the array.

#### aVeryBigSum function will take parameters a and ar which are the count of the array and the array respectively.

 code with an example. Consider the following input:

```python
def aVeryBigSum(a,ar):
    value=0
    for i in range(a):
        value+=ar[i]
    return value

```
 The aVeryBigSum function will perform the following steps:

 Example input: 5
                1000000001 1000000002 1000000003 1000000004 1000000005

 Return the integer sum of the elements in the array: 5000000015

#### Sample input & output
input
```
5
1000000001 1000000002 1000000003 1000000004 1000000005
```
output
```
5000000015
```
****


