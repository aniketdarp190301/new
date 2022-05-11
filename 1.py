import time

#Lists representing each tower
A = []
B = []
C = []

# Calculate total moves
moves = 0

# Function to move discs
def move(n, src, dest, aux):
  global moves
  # Base Case
  if (n > 0):
    move(n-1, src, aux, dest)
    dest.append(src.pop())
    moves += 1
    print(A, B, C, "\n-----------------")
    move(n-1, aux, dest, src)

# User input for number of discs
n = int(input("Enter the total number of discs: "))

for i in range(n,0,-1):
  A.append(i)

print("Initial Position: \n",A, B, C,"\n---------------")

startTime = time.time()
move(n, A, C, B)
print(f"Time Elapsed: {time.time() - startTime} seconds" )
print("Number of moves: ", moves)