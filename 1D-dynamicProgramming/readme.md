Tips:  
1. If considering previous answer =>　recursion  
2. Define your function purpose  
3. Write formula and draw the recursion tree  
(the tree is often drawn by a combination of possibility of your purpose)  
4. Be aware of your boundaries  
5. memomization with dic better than list 


[Coin change]  
print(s.coinChange([1,2,5],11))  
   f(11) #  min combination of index 11  
f(10) f(9) f(6)

[House robber]  
        f(0) # max profit of index 0  
    f(1)  f(2)

[Longest increasing subsequence]  
        f(0) #  max length of index 0       
    1  f(1)  f(2) f(3)


[Knapsack problem]  
      f(0,8) # max profit under index 0 and capacity 8  
    f(1,5) f(1,8)    