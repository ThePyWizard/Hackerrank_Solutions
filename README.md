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


## 6. Super Reduced String

  - [Problem](https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](superreducedstring.py) (navigate to the Solution file)
  - Explanation:
  >Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match,    and delete them.
  Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String

#### The superReducedString function takes an input string and iteratively removes adjacent matching characters until no more matches can be found. It returns the resulting string or "Empty String" if the final string is empty.

 code with an example. Consider the following input:

```python
def superReducedString(s):
    sample=[]
    for i in s:
        if sample and sample[-1] == i:
            sample.pop()
        else:
            sample.append(i)
    if not sample:
        return "Empty String"
    else:
        return ''.join(sample)

```
 The superReducedString function will perform the following steps:
  Initialize a stack and we can iterate through the input string.
  And remove adjacent matching characters from the string by using the stack. If the final string is empty, return "Empty String."
  If not empty, return the resulting string without adjacent matching characters.

 Example input: aaabccddd

 Return the reduced string: abd

#### Sample input & output
input
```
aaabccddd
```
output
```
abd
```
****


## 7. Flatland Space Stations

  - [Problem](https://www.hackerrank.com/challenges/flatland-space-stations/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](flatlandspacestations.py) (navigate to the Solution file)
  - Explanation:
  >Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of 1km length connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city. Determine the maximum distance from any city to its nearest space station.

#### The flatlandSpaceStations function takes an input n that is the number of cities and c[m] which is the indices of cities with a space station and determine the maximum distance from any city to its nearest space station.

 code with an example. Consider the following input:

```python
def flatlandSpaceStations(n, c):
    c.sort()
    prev_st=c[0]
    max_dist=c[0]
    for i in range(1,len(c)):
        current_st=c[i]
        dist=(current_st-prev_st)//2
        max_dist=max(max_dist,dist)
        prev_st=current_st
    max_dist=max(max_dist,n-1-prev_st)
    return max_dist

```
 The superReducedString function will perform the following steps:
  First we need to sort the space station locations (c) and then initialize max_distance to 0.
  After that, start with the first space station (prev_station) at the first element of c and calculate the distance from the first city to the first space station and set it as max_distance.
  Then iterate through the sorted space station locations:
  a. Calculate the distance from the current space station to the previous one.
  b. Update max_distance if the new distance is larger.
  c. Update prev_station for the next iteration.
  Check the distance between the last space station and the last city.
  Return the final max_distance, representing the farthest city from its nearest space station.

 Example input: 6 6
                0 1 2 4 3 5

 Returns the max distance: 0

#### Sample input & output
input
```
6 6
0 1 2 4 3 5
```
output
```
0
```
****


## 7. Pairs

  - [Problem](https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](pairs.py) (navigate to the Solution file)
  - Explanation:
  >Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

#### The pairs function takes an input of k where k is an integer and arr is an array of integers. and it returns the pair from the array whose difference equal to the target value of k.

 code with an example. Consider the following input:

```python
def pairs(k, arr):
    a=set(arr)
    count=0
    for i in arr:
        if i+k in a:
            count+=1
    return count

```
The pairs function will perform the following steps:
It creates a set called unique_elements to store the unique values from the given array arr and then initialize a variable count to 0 to keep track of the count of pairs with a difference of k.
And when we iterate through the elements in the arr:
For each element num, we check if num + k is present in the unique_elements set.
If num + k exists in the set, it means there is a pair with a difference of k. Increment the count by 1.
Then return the final value of count, which represents the count of pairs with a difference of k.

 Example input: 5 2
                1 5 3 4 2

 Returns the max distance: 3

#### Sample input & output
input
```
5 2
1 5 3 4 2
```
output
```
3
```
****
