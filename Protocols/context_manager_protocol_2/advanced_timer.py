from time import perf_counter
class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = perf_counter() - self.start
        self.last_run = self.elapsed
        self.runs.append(self.elapsed)
        self.min = min(self.runs)
        self.max = max(self.runs)

timer = AdvancedTimer()

print(timer.runs)
print(timer.last_run)
print(timer.min)
print(timer.max)

# Valid output
# []
# None
# None
# None

from time import sleep

timer = AdvancedTimer()

with timer:
    sleep(1.5)
print(round(timer.last_run, 1))

with timer:
    sleep(0.7)
print(round(timer.last_run, 1))

with timer:
    sleep(1)
print(round(timer.last_run, 1))
# Valid output
# 1.5
# 0.7
# 1.0