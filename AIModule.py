from copy import deepcopy
from queue import PriorityQueue
from Point import Point
import math

'''AIModule Interface
createPath(map map_) -> list<points>: Adds points to a path'''
class AIModule:

	def createPath(self, map_):
		pass

'''
A sample AI that takes a very suboptimal path.
This is a sample AI that moves as far horizontally as necessary to reach
the target, then as far vertically as necessary to reach the target.
It is intended primarily as a demonstration of the various pieces of the
program.
'''

class StupidAI(AIModule):

	def createPath(self, map_):
		path = []
		explored = []
		# Get starting point
		path.append(map_.start)
		current_point = deepcopy(map_.start)

		# Keep moving horizontally until we match the target
		while(current_point.x != map_.goal.x):
			# If we are left of goal, move right
			if current_point.x < map_.goal.x:
				current_point.x += 1
			# If we are right of goal, move left
			else:
				current_point.x -= 1
			path.append(deepcopy(current_point))

		# Keep moving vertically until we match the target
		while(current_point.y != map_.goal.y):
			# If we are left of goal, move right
			if current_point.y < map_.goal.y:
				current_point.y += 1
			# If we are right of goal, move left
			else:
				current_point.y -= 1
			path.append(deepcopy(current_point))

		# We're done!
		return path

class Djikstras(AIModule):

	def createPath(self, map_):
		q = PriorityQueue()
		cost = {}
		prev = {}
		explored = {}
		for i in range(map_.width):
			for j in range(map_.length):
				cost[str(i)+','+str(j)] = math.inf
				prev[str(i)+','+str(j)] = None
				explored[str(i)+','+str(j)] = False
		current_point = deepcopy(map_.start)
		current_point.comparator = 0
		cost[str(current_point.x)+','+str(current_point.y)] = 0
		q.put(current_point)
		while q.qsize() > 0:
			# Get new point from PQ
			v = q.get()
			if explored[str(v.x)+','+str(v.y)]:
				continue
			explored[str(v.x)+','+str(v.y)] = True
			# Check if popping off goal
			if v.x == map_.getEndPoint().x and v.y == map_.getEndPoint().y:
				break
			# Evaluate neighbors
			neighbors = map_.getNeighbors(v)
			for neighbor in neighbors:
				alt = map_.getCost(v, neighbor) + cost[str(v.x)+','+str(v.y)]
				if alt < cost[str(neighbor.x)+','+str(neighbor.y)]:
					cost[str(neighbor.x)+','+str(neighbor.y)] = alt
					neighbor.comparator = alt
					prev[str(neighbor.x)+','+str(neighbor.y)] = v
				q.put(neighbor)

		path = []
		while not(v.x == map_.getStartPoint().x and v.y == map_.getStartPoint().y):
			path.append(v)
			v = prev[str(v.x)+','+str(v.y)]
		path.append(map_.getStartPoint())
		path.reverse()
		return path

class AStarExp(AIModule):

	def createPath(self, map_):
		q = PriorityQueue()
		cost = {}
		prev = {}
		explored = {}
		for i in range(map_.width):
			for j in range(map_.length):
				cost[str(i) + ',' + str(j)] = math.inf
				prev[str(i) + ',' + str(j)] = None
				explored[str(i) + ',' + str(j)] = False
		current_point = deepcopy(map_.start)
		current_point.comparator = 0
		cost[str(current_point.x) + ',' + str(current_point.y)] = 0
		q.put(current_point)
		while q.qsize() > 0:
			v = q.get()
			if explored[str(v.x)+','+str(v.y)]:
				continue
			explored[str(v.x) + ',' + str(v.y)] = True
			if v.x == map_.getEndPoint().x and v.y == map_.getEndPoint().y:
				break
			neighbors = map_.getNeighbors(v)
			for neighbor in neighbors:
				if map_.getTile(neighbor.x, neighbor.y) < map_.getTile(map_.getEndPoint().x, map_.getEndPoint().y):
					h = math.sqrt(math.pow(neighbor.x - map_.getEndPoint().x, 2) + math.pow(neighbor.y - map_.getEndPoint().y, 2)) / math.sqrt(2) * math.pow(2, map_.getTile(neighbor.x, neighbor.y) - map_.getTile(map_.getEndPoint().x, map_.getEndPoint().y)) - 1
				else:
					h = math.sqrt(math.pow(neighbor.x - map_.getEndPoint().x, 2) + math.pow(neighbor.y - map_.getEndPoint().y, 2)) / math.sqrt(2)
				alt = map_.getCost(v, neighbor) + cost[str(v.x) + ',' + str(v.y)]
				if alt < cost[str(neighbor.x) + ',' + str(neighbor.y)]:
					cost[str(neighbor.x) + ',' + str(neighbor.y)] = alt
					neighbor.comparator = alt + h
					prev[str(neighbor.x) + ',' + str(neighbor.y)] = v
				q.put(neighbor)
		path = []
		while not(v.x == map_.getStartPoint().x and v.y == map_.getStartPoint().y):
			path.append(v)
			v = prev[str(v.x) + ',' + str(v.y)]
		path.append(map_.getStartPoint())
		path.reverse()
		return path


class AStarDiv(AIModule):

	def createPath(self, map_):
		q = PriorityQueue()
		cost = {}
		prev = {}
		explored = {}
		for i in range(map_.width):
			for j in range(map_.length):
				cost[str(i) + ',' + str(j)] = math.inf
				prev[str(i) + ',' + str(j)] = None
				explored[str(i) + ',' + str(j)] = False
		current_point = deepcopy(map_.start)
		current_point.comparator = 0
		cost[str(current_point.x) + ',' + str(current_point.y)] = 0
		q.put(current_point)
		while q.qsize() > 0:
			v = q.get()
			if explored[str(v.x)+','+str(v.y)]:
				continue
			explored[str(v.x) + ',' + str(v.y)] = True
			if v.x == map_.getEndPoint().x and v.y == map_.getEndPoint().y:
				break
			neighbors = map_.getNeighbors(v)
			for neighbor in neighbors:
				if map_.getTile(neighbor.x, neighbor.y) < map_.getTile(map_.getEndPoint().x, map_.getEndPoint().y):
					h = math.sqrt(math.pow(neighbor.x - map_.getEndPoint().x, 2) + math.pow(neighbor.y - map_.getEndPoint().y, 2)) / math.sqrt(2) * map_.getTile(map_.getEndPoint().x, map_.getEndPoint().y) / (1 + map_.getTile(neighbor.x, neighbor.y))
				else:
					h = math.sqrt(math.pow(neighbor.x - map_.getEndPoint().x, 2) + math.pow(neighbor.y - map_.getEndPoint().y, 2)) / math.sqrt(2)
				alt = map_.getCost(v, neighbor) + cost[str(v.x) + ',' + str(v.y)]
				if alt < cost[str(neighbor.x) + ',' + str(neighbor.y)]:
					cost[str(neighbor.x) + ',' + str(neighbor.y)] = alt
					neighbor.comparator = alt + h
					prev[str(neighbor.x) + ',' + str(neighbor.y)] = v
				q.put(neighbor)
		path = []
		while not(v.x == map_.getStartPoint().x and v.y == map_.getStartPoint().y):
			path.append(v)
			v = prev[str(v.x) + ',' + str(v.y)]
		path.append(map_.getStartPoint())
		path.reverse()
		return path
