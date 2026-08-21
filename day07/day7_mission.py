# ==========================================
# AGENTIC MISSION
# ==========================================
from collections import Counter
from collections import deque
from collections import defaultdict

# ==========================================
# 1. WORD FREQUENCY COUNTER
# ==========================================

class WFC:
    # Store the words inside the object
    def __init__(self, words):
        self.words = words

    # Display the words stored in the object
    def show_words(self):
        print(self.words)

    # Counter counts how many times each word appears
    def count_words(self):
        return Counter(self.words)


# Create a list of words to analyze
words = ["python", "django", "python"]

# Create a WFC object using the list
counter = WFC(words)

# Display the words
counter.show_words()

# Count the frequency of each word
counts = counter.count_words()

print(counts)

# Access the count of a specific word
counts["python"]

print(counts["python"])

# Get the most common word
counts.most_common(1)

print(counts.most_common(1))


# Test an empty list
empty_words = []

empty = WFC(empty_words)

print(empty.count_words())


# Test a single-element list
single_element = ["python"]

single = WFC(single_element)

print(single.count_words())


# Test two words with equal frequencies (a tie)
tie_elements = ["python", "django", "python", "django"]

tie = WFC(tie_elements)

print(tie.count_words())


# ==========================================
# 2. TASK QUEUE
# ==========================================

class TaskQueue:
    # Create an empty deque to store tasks
    def __init__(self):
        self.queue = deque()

    # Add a task to the right side
    def add_task(self, task):
        self.queue.append(task)

    # Remove and return the task from the left side
    # append() + popleft() gives FIFO behavior
    def process_task(self):
        return self.queue.popleft()

    # Add a task to the left side
    def add_task_left(self, task):
        self.queue.appendleft(task)

    # Remove and return the task from the right side
    # appendleft() + pop() also gives FIFO behavior
    def process_task_right(self):
        return self.queue.pop()


# Create a normal task queue
q = TaskQueue()

print(q.queue)

# Add tasks in order
q.add_task("A")

q.add_task("B")

q.add_task("C")

print(q.queue)

# Process tasks using FIFO
print(q.process_task())

print(q.process_task())

print(q.process_task())

print(q.queue)


# Test the opposite deque operations
p = TaskQueue()

# Add tasks from the left
p.add_task_left("A")

p.add_task_left("B")

p.add_task_left("C")

print(p.queue)

# Remove tasks from the right
print(p.process_task_right())

print(p.process_task_right())

print(p.process_task_right())

print(p.queue)


# ==========================================
# 3. GRAPH
# ==========================================

class Graph:
    # Create an adjacency list using defaultdict(list)
    # Missing nodes automatically get an empty list
    def __init__(self):
        self.graph = defaultdict(list)

    # Add a directed edge from source to destination
    # Example: A -> B
    def add_edge(self, source, destination):
        self.graph[source].append(destination)


# Create an empty graph
g = Graph()

print(g.graph)

# Add graph edges
g.add_edge("A", "B")

g.add_edge("A", "C")

g.add_edge("C", "D")

print(g.graph)

# Accessing X creates an empty list because
# the graph uses defaultdict(list)
g.graph["X"]

# Add a self-loop: A -> A
g.add_edge("A", "A")

print(g.graph)
