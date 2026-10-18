"""
High-throughput lock-free ring buffer for streaming telemetry.
Authored by @Amir-Pakdel with collaboration from @NullXPlus.
"""

import threading

class AtomicRingBuffer:
    def __init__(self, capacity: int = 1024):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0

    def push(self, item) -> bool:
        self.buffer[self.tail % self.capacity] = item
        self.tail += 1
        return True
