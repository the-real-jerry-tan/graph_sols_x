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

# Test harness for the graph problems

from graph_problem_1 import dfs
from graph_problem_2 import bfs_shortest_path
from graph_problem_3 import has_cycle

def run_tests():
    # Problem 1 Test Cases: DFS path existence
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    assert dfs(graph, 'A', 'F') == True, "Test Case 1 Failed"
    assert dfs(graph, 'A', 'D') == True, "Test Case 2 Failed"
    assert dfs(graph, 'E', 'A') == False, "Test Case 3 Failed"
    
    # Problem 2 Test Cases: BFS shortest path
    assert bfs_shortest_path(graph, 'A', 'F') == ['A', 'C', 'F'], "Test Case 4 Failed"
    assert bfs_shortest_path(graph, 'A', 'D') == ['A', 'B', 'D'], "Test Case 5 Failed"
    
    # Problem 3 Test Cases: Cycle detection
    cyclic_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    acyclic_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': []
    }
    assert has_cycle(cyclic_graph) == True, "Test Case 6 Failed"
    assert has_cycle(acyclic_graph) == False, "Test Case 7 Failed"
    
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
