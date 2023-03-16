# opof-grid2d

[OPOF](https://github.com/opoframework/opof) simple navigation domains in a 2D grid world to help users familiarize with OPOF. They also act as a sanity check for developing optimization algorithms.

[![Build and Test](https://github.com/opoframework/opof-grid2d/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/opoframework/opof-grid2d/actions/workflows/build_and_test.yml)

`opof-grid2d` is maintained by the [Kavraki Lab](https://www.kavrakilab.org/) at Rice University.

### Installation
```console
$ pip install opof-grid2d
```

`opof-grid2d` is officially tested and supported for Python 3.9, 3.10, 3.11.

## Domain: `RandomWalk2D[size]`
<p align="left">
    <img src="https://github.com/opoframework/opof-grid2d/blob/master/docs/_static/img/random_walk2d.svg?raw=true" width="250px"/>
</p>

```python
from opof_grid2d.domains import RandomWalk2D
domain = RandomWalk2D(11) # Creates a RandomWalk2D domain instance for a 11x11 board.
```

##### Description
An agent starts at a location (green) and moves in random directions according to some fixed probabilities until it reaches the goal (magenta). 
When attempting to move _into_ an obstacle (black) or the borders of the grid, a step is spent but the position of the agent does not change. 
The probability of moving in each direction is fixed across all steps. 

##### Planner optimization problem
We want to find a generator that maps a problem instance $c$ (in this case, the combination of board layout and start and goal positions) into direction probabilities (in this case, vectors $\in \mathbb{R}^4$ with non-negative entries summing to $1$), such that the number of steps taken during the random 
walk is minimized.

##### Planning objective
$\boldsymbol{f}(x; c)$ is given as $- steps / (4 \times size^2)$, where $steps$ is the number of steps taken to reach the goal. A maximum of $4 \times size^2$ steps are allowed.

##### Problem instance distribution
The training set and testing set each contain $1000$ problem instances, where the obstacle, start, and goal positions 
are uniformly sampled. 

## Domain: `Maze2D[size]`
<p align="left">
    <img src="https://github.com/opoframework/opof-grid2d/blob/master/docs/_static/img/maze2d.svg?raw=true" width="250px"/>
</p>

```python
from opof_grid2d.domains import Maze2D
domain = Maze2D(11) # Creates a Maze2D domain instance for a 11x11 board.
```

##### Description
[A* search](https://en.wikipedia.org/wiki/A*_search_algorithm) is run against a _heuristic_ function $h(n)$ to find a path from the start (green) to the goal (green). The heuristic function determines the priority in which nodes are expanded (cells that are in darker red have a lower $g(n) + h(n)$ value, and have higher priority). The maze is assumed to be _perfect_, i.e., there is exactly one path between any two cells. 

##### Planner optimization problem
We want to find a generator $G_\theta(c)$ that maps a problem instance $c$ (in this case, the combination of board layout and start and goal positions) to $h(n)$ (in this case, assignments of values $\in [0, size^2]$ to each of the $size^2$ cells) such that the number of nodes expanded in the A* search is minimized. 

##### Planning objective
The planning objective $\boldsymbol{f}(x; c)$ is given as $- steps / n_{\mathrm{empty}}$, where $steps$ is the number of nodes expanded before finding the goal and $n_{\mathrm{empty}}$ is the number of obstacle-free cells. 

##### Problem instance distribution
The training set and testing set each contain $1000$ problem instances, where the maze is generated using [Wilson's algorithm](https://dl.acm.org/doi/10.1145/237814.237880), and the start and goal positions are uniformly sampled.


## Citing
If you use `opof-grid2d`, please cite us with:

```
@article{lee23opof,
  author = {Lee, Yiyuan and Lee, Katie and Cai, Panpan and Hsu, David and Kavraki, Lydia E.},
  title = {The Planner Optimization Problem: Formulations and Frameworks},
  booktitle = {arXiv},
  year = {2023},
  doi = {10.48550/ARXIV.2303.06768},
}
```

## License

`opof-grid2d` is licensed under the [BSD-3 license](https://github.com/opoframework/opof-grid2d/blob/master/LICENSE.md).

`opof-grid2d` is maintained by the [Kavraki Lab](https://www.kavrakilab.org/) at Rice University, funded in part by NSF RI 2008720 and Rice University funds.
