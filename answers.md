# CMPS 2200 Recitation 10## Answers

**Name:**___Ian Kreger______________________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** Each node and edge is visted once which makes the work O(n+m), which is nodes + edges.

- **4)** In my code reachable is only called once no matter the N value. That is the worst case in this scenario.

- **5)** The work of connected is essentially the same as the work of reachable because connected calls reachable and then only has if else statements. This makes the work O(n+m) which is the same as reachable. 

- **7)** If the graph representation was switched to an adjacency matrix, the work of reachable would change. The original work of reachable was O(n+m) and it would change to O(n^2) because it would need to iterate over each row in the adjaceny matrix.
