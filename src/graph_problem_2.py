# /**
#  * © 2024 Jerry Tan. All Rights Reserved.
#  *
#  * This software is the confidential and proprietary information of Jerry Tan
#  * ("Confidential Information"). You shall not disclose such Confidential Information
#  * and shall use it only in accordance with the terms under which this software
#  * was distributed or otherwise published, and solely for the prior express purposes
#  * explicitly communicated and agreed upon, and only for those specific permissible purposes.
#  *
#  * This software is provided "AS IS," without a warranty of any kind. All express or implied
#  * conditions, representations, and warranties, including any implied warranty of merchantability,
#  * fitness for a particular purpose, or non-infringement, are disclaimed, except to the extent
#  * that such disclaimers are held to be legally invalid.
#  */

# Problem 2: Breadth-First Search to find the shortest path in an unweighted graph

from collections import deque

def bfs_shortest_path(graph, start, goal):
    """
    Breadth-First Search (BFS) to find the shortest path between two nodes in an unweighted graph.
    
    Args:
        graph (dict): Adjacency list representation of the graph.
        start (str): Starting node.
        goal (str): Target node.
    
    Returns:
        list: List of nodes in the shortest path.
    """
    # Maintain a queue of paths
    queue = deque([[start]])
    
    # Set to store visited nodes
    visited = set()
    
    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        
        # Get the last node from the path
        node = path[-1]
        
        # Return the path if we reached the goal
        if node == goal:
            return path
        
        # Check all adjacent nodes and add new paths to the queue
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                visited.add(neighbor)
    
    return None
