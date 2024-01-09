classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]


def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    if (email is None):
        email = f'{name}@example.com'
    classroom.append({'name': name, 'email': email.lower(), 'grade': []})


def find_student(name):
    for i, s in enumerate(classroom):
        if s['name'] == name:
            return i
    return -1


def delete_student(name):
    """Delete a student from the classroom"""
    index = find_student(name)
    del classroom[index]


def set_email(name, email):
    """Sets the email of the student"""
    index = find_student(name)
    classroom[index]['email'] = email.lower()


def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    index = find_student(name)
    classroom[index]['grades'].append((profession, grade))


def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """
    sum, count = 0, 0
    index = find_student(name)
    for g in classroom[index]['grades']:
        if g[0] == profession:
            sum += g[1]
            count += 1
    return sum / count


def get_professions(name):
    """Returns a list of unique professions that student has grades in"""
    index = find_student(name)
    return list({pro for pro, _ in classroom[index]['grades']})
