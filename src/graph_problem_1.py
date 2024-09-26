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

# Problem 1: Depth-First Search to check if a path exists between two nodes

def dfs(graph, start, goal, visited=None):
    """
    Depth-First Search (DFS) to find if a path exists between two nodes in a graph.
    
    Args:
        graph (dict): Adjacency list representation of the graph.
        start (str): Starting node.
        goal (str): Target node.
        visited (set): Set of visited nodes.
    
    Returns:
        bool: True if a path exists, otherwise False.
    """
    if visited is None:
        visited = set()
    
    # Mark current node as visited
    visited.add(start)
    
    # If the goal is found, return True
    if start == goal:
        return True
    
    # Recur for all adjacent vertices
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    
    return False
