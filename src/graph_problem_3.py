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

# Problem 3: Detect Cycle in a Directed Graph using Depth-First Search

def has_cycle(graph):
    """
    Detect if a cycle exists in a directed graph using DFS.
    
    Args:
        graph (dict): Adjacency list representation of the graph.
    
    Returns:
        bool: True if the graph has a cycle, otherwise False.
    """
    visited = set()
    rec_stack = set()
    
    def dfs(node):
        if node in rec_stack:
            return True
        if node in visited:
            return False
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        rec_stack.remove(node)
        return False
    
    for node in graph:
        if dfs(node):
            return True
    return False
