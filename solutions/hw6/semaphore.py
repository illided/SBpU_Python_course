from threading import Condition


class Semaphore:
    """
    Primitive sync tool. When using with context manager
    locks code block, so only one thread could access it.
    When job is done lock is released
    """

    entered: bool
    condition: Condition

    def __init__(self):
        self.condition = Condition()
        self.entered = False

    def __enter__(self):
        with self.condition:
            self.condition.wait_for(lambda: not self.entered)
        self.entered = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.entered = False
