import unittest
import todo


class TestRemoveTask(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            {"task": "Task 1", "completed": False},
            {"task": "Task 2", "completed": True},
            {"task": "Task 3", "completed": False}
        ]


if __name__ == '__main__':
    unittest.main()
