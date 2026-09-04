from day13.mission import chunked, pipeline, read_lines, double, stringify, add_ten, count, islice
import psutil

def test_chunked():
    chunks = chunked(range(10), 3)

    assert next(chunks) == [0, 1, 2]
    assert next(chunks) == [3, 4, 5]
    assert next(chunks) == [6, 7, 8]
    assert next(chunks) == [9]

def test_chunked_is_lazy():
    produced = []

    def source():
        for number in range(10):
            produced.append(number)
            yield number

    chunks = chunked(source(), 3)

    assert produced == []

    assert next(chunks) == [0, 1, 2]
    assert produced == [0, 1, 2]

def test_pipeline():
    result = pipeline(
        [1, 2, 3],
        double,
        add_ten,
        stringify,
    )

    assert list(result) == ["12", "14", "16"]

def test_pipeline_middle_stage():
    def add_twenty(numbers):
        for number in numbers:
            yield number + 20

    result = pipeline(
        [1, 2, 3],
        double,
        add_twenty,
        stringify,
    )

    assert list(result) == ["22", "24", "26"]

def test_read_lines_memory(tmp_path):
    path = tmp_path / "large.log"

    with open(path, "w") as file:
        for _ in range(100):
            file.write("A\n" * (1024 * 1024 // 2))

    process = psutil.Process()
    before = process.memory_info().rss

    lines = read_lines(path)

    for _ in lines:
        pass

    after = process.memory_info().rss

    memory_used = after - before

    assert memory_used < 10 * 1024 * 1024

def test_islice_limits_infinite_generator():
    numbers = count(1)

    result = list(islice(numbers, 10))

    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
