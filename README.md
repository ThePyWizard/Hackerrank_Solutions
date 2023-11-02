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
 It will take array length and the array as input and will add the array elements and will return the longint sum of the array elements.

 Example input: 5
                1000000001 1000000002 1000000003 1000000004 1000000005

 Return the integer sum of the elements in the array: 5000000015

#### Sample input & output
input
```
5 6 7
3 6 10
```
output
```
1 1
```
****

## 2. Compare the Triplets

  - [Problem](https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](comparethetriplets.py) (navigate to the Solution file)
  - Explanation:
  >The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
    If a[i] > b[i], then Alice is awarded 1 point.
    If a[i] < b[i], then Bob is awarded 1 point.
    If a[i] = b[i], then neither person receives a point.
    Comparison points is the total points a person earned.

#### Compare The Triplets function will take parameters a and b which are the array of values of Alice and Bob.

 code with an example. Consider the following input:

```python
def compareTriplets(a, b):
    score_a=0
    score_b=0
    res=[]
    for i in range(len(a)):
        if a[i]>b[i]:
            score_a+=1
        elif a[i]<b[i]:
            score_b+=1
    res.extend([score_a,score_b])
    return res
        

```
 The compareTriplets function will perform the following steps:
 It will consider score_a and score_b initially as zero. and using for loop it iterates through the elements and compare each and increments the score values using the if-else conditions mentioned.
 And then it adds both score into an array and return the array.

 Example input: 17 28 30
                99 16 8

 Return the score of Alice and Bob: 2 1

#### Sample input & output
input
```
17 28 30
99 16 8
```
output
```
2 1
```
****


