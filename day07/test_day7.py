# ==========================================
# DAY 7 — PYTEST TESTS
# ==========================================

from day7_mission import WFC, TaskQueue, Graph


# ==========================================
# 1. WFC TESTS
# ==========================================

# Test normal word counting
def test_wfc_count():
    words = ["python", "django", "python"]
    c = WFC(words)
    counts = c.count_words()

    # Python should appear twice
    assert counts["python"] == 2

    # Django should appear once
    assert counts["django"] == 1


# Test that empty input produces an empty Counter
def test_wfc_empty():
    empty = []
    e = WFC(empty)
    counts = e.count_words()

    assert len(counts) == 0


# Test counting a single word
def test_wfc_single():
    single_element = ["python"]
    single = WFC(single_element)
    s = single.count_words()

    # There should be one unique word
    assert len(s) == 1

    # That word should have a frequency of one
    assert s["python"] == 1


# Test a tie where two words have the same frequency
def test_wfc_ties():
    words = ["python", "django", "python", "django"]
    ties = WFC(words)
    t = ties.count_words()

    # Both words should appear twice
    assert t["python"] == 2
    assert t["django"] == 2


# ==========================================
# 2. TASK QUEUE TESTS
# ==========================================

# Test FIFO behavior using append() and popleft()
def test_taskqueue():
    q = TaskQueue()

    q.add_task("A")
    q.add_task("B")
    q.add_task("C")

    # Tasks must come out in the same order they were added
    assert q.process_task() == "A"
    assert q.process_task() == "B"
    assert q.process_task() == "C"


# Test FIFO behavior using appendleft() and pop()
def test_taskqueue_right():
    q = TaskQueue()

    q.add_task_left("A")
    q.add_task_left("B")
    q.add_task_left("C")

    # Even though tasks were added from the left,
    # pop() processes them in FIFO order
    assert q.process_task_right() == "A"
    assert q.process_task_right() == "B"
    assert q.process_task_right() == "C"


# ==========================================
# 3. GRAPH TESTS
# ==========================================

# Test normal graph edges
def test_graph_edges():
    g = Graph()

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("C", "D")

    # A should be connected to B and C
    assert "B" in g.graph["A"]
    assert "C" in g.graph["A"]

    # C should be connected to D
    assert "D" in g.graph["C"]


# Test a disconnected node
def test_graph_disconnected():
    g = Graph()

    # Accessing a missing key creates an empty list
    # because the graph uses defaultdict(list)
    g.graph["X"]

    # X exists but has no outgoing edges
    assert g.graph["X"] == []


# Test a self-loop where a node points to itself
def test_graph_self_loop():
    g = Graph()

    g.add_edge("A", "A")

    # A should contain itself in its adjacency list
    assert "A" in g.graph["A"]