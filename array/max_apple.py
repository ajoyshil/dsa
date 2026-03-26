"""
Alice and Bob work in a beautiful orchard. There are N apple trees in the orchard. The apple trees are arranged in a row
 and they are numbered from
1 to N.
Alice is planning to collect all the apples from K consecutive trees and Bob is planning to collect all the apples from
L consecutive trees. They want
to choose two disjoint segments (one consisting of K trees for Alice and the other consisting of L trees for Bob) so as
not to disturb each other.
What is the maximum number of apples that they can collect?
Write a function:
def solution(A, K, L)
that, given an array A consisting of N integers denoting the number of apples on each apple tree in the row, and
integers K and L denoting,
respectively, the number of trees that Alice and Bob can choose when collecting, returns the maximum number of apples
that can be collected by
them, or −1 if there are no such intervals.
For example, given A = [6, 1, 4, 6, 3, 2, 7, 4], K = 3, L = 2, your function should return 24, because Alice can choose
trees 3 to 5 and collect 4 + 6 + 3 =
13 apples, and Bob can choose trees 7 to 8 and collect 7 + 4 = 11 apples. Thus, they will collect 13 + 11 = 24 apples in
total, and that is the maximum
number that can be achieved.
Given A = [10, 19, 15], K = 2, L = 2, your function should return −1, because it is not possible for Alice and Bob to
choose two disjoint intervals.
Assume that:
N is an integer within the range [2..100];
K and L are integers within the range [1..N - 1];
each element of array A is an integer within the range [1..500].

"""

def brute_force(A, K, L):
  """
  Brute-force solution to find the maximum apples Alice and Bob can collect.

  Args:
      A: Array of apple counts on N trees.
      K: Number of trees Alice can choose.
      L: Number of trees Bob can choose.

  Returns:
      Maximum apples both can collect, or -1 if no disjoint intervals.
  """
  N = len(A)
  max_apples = -float('inf')
  if N < K + L:
      return -1
  # Loop through all possible starting points for Alice.
  for alice_start in range(0, N - L + 1):
    # Loop through all possible starting points for Bob (non-overlapping).
    for bob_start in range(alice_start+K, N):
      # Check if intervals are valid (no overlap).
      if alice_start + K - 1 < bob_start :
        # Calculate total apples for Alice and Bob.
        alice_apples = sum(A[alice_start:alice_start + K])
        bob_apples = sum(A[bob_start:bob_start + L])
        # Update maximum apples if current total is higher.
        max_apples = max(max_apples, alice_apples + bob_apples)

  # Return maximum apples or -1 if no valid intervals found.
  return max_apples if max_apples != -float('inf') else -1


A = [6, 1, 4, 6, 3, 2, 7, 4]
# A = [10, 19, 15]
K = 3
L = 2

print(brute_force(A, K, L))
