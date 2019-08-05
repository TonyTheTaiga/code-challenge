/*
 * @lc app=leetcode id=509 lang=cpp
 *
 * [509] Fibonacci Number
 */
class Solution {
public:
    int fib(int N) {
        if (N > 1) {return fib(N - 1) + fib(N - 2);}
        else {return N;}
    }
};

