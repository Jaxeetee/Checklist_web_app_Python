filePath = 'todos.txt'


def read_todos_file() -> list[str]:
    """
    Functions that reads the todos.txt file
    :return:
    """
    with open(filePath, 'r') as file_read:
        return file_read.readlines()


def update_todos_file(todoList):
    """
    Function that updates the todos.txt file
    """
    with open(filePath, 'w') as file_write:
        file_write.writelines(todoList)