from scarab import scarab

from conftest import TESTS_DIR


def test_main():
    assert scarab.main([str(TESTS_DIR / "testdata" / "example_task.py")]) == 0
