import sys
import random


def main():
    # TODO: your code here

    # 1. Get the command line arguments via sys.argv

    # 2. Open the correct file open(rf'questions\<filename>.txt)'

    # 3. Iterate over the file

    #       3.1. Parse the line (use s.split())
    #       3.2 Create a list of options
    #       3.3 random.shuffle(l)

    print(sys.argv)
    file_name = sys.argv[1]
    num = int(sys.argv[2])

    listQ = convert_file_to_objects(file_name)

    count = 0
    for n in range(num):
       count += print_question(listQ[n])

    print(f'You answer {count}/{num} correct answers')


# create question list
def convert_file_to_objects(file_name):

    listQ = []
    with open(rf'questions/{file_name}') as file:
        for line in file:
            (question, answer, options) = line.split(';')
            question = question.strip()
            answer = answer.strip()
            optionsList = options.split(',')
            optionsList = [o.strip() for o in optionsList]
            optionsList.append(answer)
            random.shuffle(optionsList)
            listQ.append({'question': question, 'answer': answer, 'optionsList': optionsList})

    random.shuffle(listQ)
    return listQ


# print a question, return 1 if correct, else 0
def print_question(q):
    print(q['question'])
    for i, o in enumerate(q['optionsList']):
        print(f'{i+1}. {o}')
    selected = int(input('Select the correct answer: '))
    if q['optionsList'][selected-1] == q['answer']:
        return 1
    return 0


if __name__ == '__main__':
    main()
