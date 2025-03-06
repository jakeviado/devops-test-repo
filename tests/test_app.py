import unittest
from app import plagiarism_checker


class TestPlagiarismChecker(unittest.TestCase):

    def test_similarity_score(self):
        text1 = "This is a sample text."
        text2 = "This is another example text."
        score = plagiarism_checker(text1, text2)
        self.assertGreater(score, 0)


if __name__ == "__main__":
    unittest.main()
