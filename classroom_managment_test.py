import pytest
import classroom_managment as cm


def test_add_student():
    assert len(cm.classroom) == 3
    cm.add_student('David', 'david2@example.com')
    assert len(cm.classroom) == 4
    assert cm.classroom[3]['email'] == 'david2@example.com'


def test_delete_student():
    assert len(cm.classroom) == 4
    cm.delete_student('David')
    assert len(cm.classroom) == 3


def test_set_email():
    cm.set_email('Bob', 'bob.new@example.com')
    assert cm.classroom[1]['email'] == 'bob.new@example.com'


def test_add_grade():
    cm.add_grade('Charlie', 'math', 88)
    assert ('math', 88) in cm.classroom[2]['grades']


@pytest.mark.parametrize(
    ('name', 'profession', 'avg_grade'),
    (
        ('Alice', 'math', 92),
        ('Bob', 'english', 92),
        ('Charlie', 'english', 84),
    )
)
def test_avg_grade(name, profession, avg_grade):
    assert cm.avg_grade(name, profession) == avg_grade


@pytest.mark.parametrize(
    ('student_name', 'professions'),
    (
        ('Alice', {'math', 'english', 'history'}),
        ('Bob', {'math', 'english', 'history'}),
        ('Charlie', {'english', 'history', 'physics', 'math'}),
    )
)
def test_get_professions(student_name, professions):
    assert set(cm.get_professions(student_name)) == professions


def test_add_student_with_email_none():
    assert len(cm.classroom) == 3
    cm.add_student('Eva')
    assert len(cm.classroom) == 4
    assert cm.classroom[3]['email'] == 'eva@example.com'
