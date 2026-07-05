"""
Session 22 - Program 4: N-th Tribonacci Number (Workout)

Each term is the sum of the previous three, starting T_0=0, T_1=1, T_2=1.
(LeetCode 1137.)

Sample Output:
Enter n: 4
4

Try also: n = 6 gives 13.
"""

# Program 4: N-th Tribonacci number
n = int(input("Enter n: "))
t0, t1, t2 = 0, 1, 1
if n == 0:
    print(t0)
elif n == 1 or n == 2:
    print(1)
else:
    for i in range(3, n + 1):
        t3 = t0 + t1 + t2
        t0, t1, t2 = t1, t2, t3
    print(t2)
