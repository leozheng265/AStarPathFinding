# AStarPathFinding

## Introduction

This project utilizes the A* framework to find the optimal path between two points. Two versions of A* are implemented with different cost functions as well as Dijkstra’s algorithm for comparing purposes.

## Demo

https://user-images.githubusercontent.com/61644743/195504780-e4cd5e9d-3926-4a3c-bb15-cb90f24c9980.mp4

## Cost Functions

### Exponential Cost Function:

$$
Cost = 2^{(h_1-h_0)}
$$

### Division Cost Function:

$$
Cost =\frac{h_1}{h_0 + 1}
$$

## Running Instructions

### Command line arguments:

- -w (int) - width of the map. Default 500.
- -l (int) - length of the map. Default 500.
- -seed (int) - seed to set for random terrain generation. Default none.
- -filename (string) - filename for .npy file to load for map
- -cost (string) - cost function. Values [‘exp’, ‘div’] accepted. Default ‘exp’.
- -AI (string) - Name of AIModule to use. Values [‘AStarExp’, ‘AStarDiv’, ‘Dijkstra’] accepted.

### Example Command:

```bash
python3 Main.py -seed 0 -cost exp -AI AStarExp
```

## Demo video:

https://youtu.be/O7ofCwT1OOk
