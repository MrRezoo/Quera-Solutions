import subprocess

from django.test import TestCase


def copy_content(from_, to_):
    def wrapper(test_func):
        def decorator(*args, **kwargs):
            with open(from_) as f:
                with open(to_, "w") as f1:
                    f1.write(f.read())
            test_func(*args, **kwargs)

        return decorator

    return wrapper


def empty_file(file_path):
    open(file_path, "w").close()


def run_tests():
    result = subprocess.run("python3 manage.py test classes", shell=True)
    return result


class TestAll(TestCase):
    PASSED = (0,)
    SERIALIZERS_PATH = "classes/serializers.py"
    TESTS_PATH = "classes/tests.py"

    @copy_content("classes/temp_tests_file.py", TESTS_PATH)
    def setUp(self):
        empty_file(self.SERIALIZERS_PATH)

    def tearDown(self):
        empty_file(self.TESTS_PATH)

    @copy_content("tests/sample.py", SERIALIZERS_PATH)
    def test_correct_answer(self):
        result = run_tests()
        self.the_tests_should_pass(result)

    def the_tests_should_pass(self, result):
        self.assertIn(result.returncode, self.PASSED, msg="tests failed for a correct code")
