# Josephus Problem 💥

The **Josephus Problem** is a famous theoretical problem in mathematics and computer science. It describes a situation where people stand in a circle, and every k-th person is eliminated until only one remains. This algorithm helps to determine the position of the last survivor. 

## Problem Overview 🤔
In the Josephus Problem, there are `n` people standing in a circle. The task is to eliminate every k-th person until only one person remains. The objective is to find out which position in the circle will be the last one remaining.

For example, for `n=7` and `k=3`, the sequence of eliminations will be:
- Start with 7 people: 1, 2, 3, 4, 5, 6, 7.
- Eliminate every 3rd person.
- The remaining person is the last survivor.

## Problem Statement 📜
You are given `n` people, and you need to find the position of the last remaining person if every k-th person is eliminated. For `n` people and a fixed `k=2`, the position of the last person standing can be calculated using the formula:

### Formula 🔢:
n = 2^(a) + l where a is the largest power of 2 less than n. 2l + 1 = position of the last person standing.

 
