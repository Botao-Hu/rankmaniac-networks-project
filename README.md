# rankmaniac-networks-project

PageRank is a link analysis algorithm which ranks each node in a web graph with the purpose of measuring its relative importance within the set.

In this project, we took the advantage of MapReduce to implement the ranks of nodes in a graph based on the transition matrix, a.k.a. PageRank algorithm. We used two sequential MapReduce process: PageRank step calculates and update the page ranks of each node; Process step determine the convergence condition.

In the optimization process, we carefully optimized convergence condition using "top-k convergence condition", as well as heapsort to reduce the time complexity of single iteration. More importantly, we studied the pattern of PageRank of top nodes in different iterations, and proposed our core algoritm - "linear extrapolation" strategy, which helps us to predict future PageRanks and skip iterations.

As a result, our team beated the last year champion in accuracy and efficiency. 

CS144 Network Economics course project, Caltech, spring 2017. Contributor: Botao Hu, Guanya Shi, Hangwen Lu. 