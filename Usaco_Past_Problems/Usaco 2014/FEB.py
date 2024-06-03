'''
Problem Statement:
Given a string of n text messages on a line. FJ intercepts some of these messages to the sender is unknown(could be either)
Simulate each cow in the place cow of each F to find the number of different excitement levels

Example input:
4
FEBFEBFEB

Idea:
Iterate through each possiblilty modulating things from the back
'''

n = int(input())
cows = str(input())
num = cows.count("F")

