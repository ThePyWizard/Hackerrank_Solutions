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


## 3. Diagonal Difference

  - [Problem](https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](diagonaldifference.py) (navigate to the Solution file)
  - Explanation:
  >The task is to return the absolute difference between the sums of the matrix's two diagonals as a single integer.

#### digonalDifference function takes 'a' which is the matrix size and 'arr' which is the matrix. and computes the leftsum and rightsum using forloop and returns the absolute value using abs() on the difference between leftsum and rightsum.

 code with an example. Consider the following input:

```python
def diagonalDifference(a,arr):
    leftsum=0
    rightsum=0
    for i in range(a):
        leftsum+=arr[i][i]
        rightsum+=arr[i][a-i-1]
    return abs(leftsum-rightsum)
        

```
 The Diagonal Difference function will perform the following steps:
 It takes 'a' which is the matrix size and 'arr' which is the matrix. and computes the leftsum and rightsum of diagonals using forloop and returns the absolute value using abs() on the difference between leftsum and rightsum.

 Example input: 3
                11 2 4
                4 5 6
                10 8 -12

 Return the absolute value between the sums of the matrix's two diagonals as a single integer: 15

#### Sample input & output
input
```
3
11 2 4
4 5 6
10 8 -12
```
output
```
15
```
****

## 4. The Hurdle Race

  - [Problem](https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](hurdlerace.py) (navigate to the Solution file)
  - Explanation:
  >Complete the hurdleRace function in the editor below.
    A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights, and the characters have a maximum height they can jump. There is a magic potion they can take that will increase their maximum jump height by 1 unit      for each dose. How many doses of the potion must the character take to be able to jump all of the hurdles. If the character can already clear all of the hurdles, return 0.
    hurdleRace has the following parameter(s):
    int k: the height the character can jump naturally
    int height[n]: the heights of each hurdle

#### The Hurdle Race function will return the maximum times the player has to drink the potion to jump across all hurdles.

 code with an example. Consider the following input:

```python
def hurdleRace(k, height):
    biggest_hurdle=max(height)
    if k>biggest_hurdle:
        return 0
    else:
        return biggest_hurdle-k

```
 The hurdleRace function will perform the following steps:
 It will take k which is the natural height in which the player can jump and height which is the heights of each hurdle. We will find maximum height of the hurdle using max() since height is a array and compare it with k and if k>biggest hurdle, then we will return 0 which means it doesn't take any potion to jump and else we will return biggest_hurdle-k.

 Example input: 5 4
                1 6 3 5 2

 Return amount of time potion needs to consumed: 2

#### Sample input & output
input
```
5 4
1 6 3 5 2
```
output
```
2
```
****

## 5. Ice Cream Parlor

  - [Problem](https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](icecreamparlor.py) (navigate to the Solution file)
  - Explanation:
  >Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

#### icecreamParlor function takes list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

 code with an example. Consider the following input:

```python
def icecreamParlor(m, arr):
    sample={}
    for i in range(len(arr)):
        a=arr[i]
        budget_remaining=m-a
        if budget_remaining in sample:
            return [sample[budget_remaining]+1,i+1]
        sample[a]=i
        

```
The icecreamParlor function will perform the following steps: 
This code takes two inputs: 'm' (the customer's budget) and 'arr' (a list of ice cream prices). It then iterates through the list to find two ice cream flavors whose prices add up to the customer's budget 'm'. When it finds a suitable pair, it returns the 1-based indices of these flavors, making it easy for customers to choose their desired ice cream combination.

 Example input: 2
                4
                5
                1 4 5 3 2
                4
                4
                2 2 4 3

 Return the suitable pair of icecream combination that will be on budget: 1 4
1 2

#### Sample input & output
input
```
2
4
5
1 4 5 3 2
4
4
2 2 4 3
```
output
```
1 4
1 2
```
****
