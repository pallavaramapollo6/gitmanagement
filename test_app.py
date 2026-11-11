import unittest
from app import add_student

class TestStudent(unittest.TestCase):

    def test_add_student(self):
        result = add_student("Arun")

        self.assertEqual(
            result,
            "Student added: Arun"
        )

if __name__ == "__main__":
    unittest.main()
