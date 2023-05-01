class Solution:

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Define a function maximumDetonation that takes in a list of lists called bombs and returns an integer

        visited = set()
        # Create an empty set called visited that will keep track of visited vertices during DFS

        adjList = defaultdict(list)
        # Create a defaultdict called adjList to hold the adjacency list of bombs

        Max = 0
        # Create a variable called Max to keep track of the maximum detonation

        for i in range(len(bombs)):
            # For each bomb i in the input list of bombs

            for j in range(len(bombs)):
                # For each bomb j in the input list of bombs

                distance = sqrt((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2)
                # Calculate the Euclidean distance between bombs i and j

                if i != j and bombs[i][2] >= distance:
                    # If bombs i and j are not the same and the detonation range of bomb i is greater than or equal to the distance between bombs i and j

                    adjList[i].append(j)
                    # Add bomb j to the adjacency list of bomb i

        def dfs(b):
            # Define a function dfs that takes a parameter b

            visited.add(b)
            # Add the current vertex b to the set of visited vertices

            for neighbours in adjList[b]:
                # For each neighbour of the current vertex b in the adjacency list adjList

                if neighbours not in visited:
                    # If the neighbour is not already visited

                    dfs(neighbours)
                    # Recursively call the dfs function on the neighbour

        print(adjList)
        # Print the adjacency list adjList

        for adj in range(len(bombs)):
            # For each bomb adj in the input list of bombs

            dfs(adj)
            # Call the dfs function on the current bomb adj

            print(visited)
            # Print the set of visited vertices

            Max = max(Max, len(visited))
            # Update the maximum detonation Max to be the maximum of the current Max and the length of the set of visited vertices

            visited.clear()
            # Clear the set of visited vertices for the next iteration of the loop

        return Max
        # Return the maximum detonation Max