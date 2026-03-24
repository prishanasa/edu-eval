# Unit tests for EduEval AI components

def test_marks_to_grade():
    from utils import marks_to_grade
    assert marks_to_grade(10) == "A+"
    assert marks_to_grade(8) == "A"
    assert marks_to_grade(7) == "B"
    assert marks_to_grade(5) == "C"
    assert marks_to_grade(3) == "D"
    assert marks_to_grade(1) == "F"
    print("test_marks_to_grade passed")

def test_truncate_text():
    from utils import truncate_text
    assert truncate_text("hello", 10) == "hello"
    assert truncate_text("hello world this is long", 5) == "hello..."
    print("test_truncate_text passed")

def test_validate_inputs():
    from error_handler import validate_inputs
    valid, msg = validate_inputs("What is ML?", "ML is machine learning.")
    assert valid == True
    valid, msg = validate_inputs("", "some answer")
    assert valid == False
    valid, msg = validate_inputs("What is ML?", "hi")
    assert valid == False
    print("test_validate_inputs passed")

if __name__ == "__main__":
    test_marks_to_grade()
    test_truncate_text()
    test_validate_inputs()
    print("All tests passed!")
