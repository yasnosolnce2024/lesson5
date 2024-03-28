class Task:
    def __init__(self, workname, deadline):
        self.workname = workname
        self.deadline = deadline
        self.status = False

    def mark_completion(self):
        self.status = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, workname, deadline):
        task = Task(workname, deadline)
        self.tasks.append(task)

    def mark_completion(self, workname):
        for task in self.tasks:
            if task.workname == workname:
                task.mark_completion()
                print(f'Задача "{workname}" выполнена!')
                return  # Добавлено для выхода из цикла после выполнения задачи
        print(f'Задача "{workname}" не найдена.')

    def list_unfulfilled(self):
        unfulfilled = [task for task in self.tasks if not task.status]
        if unfulfilled:
            print("Список текущих задач (не выполненные):")
            for task in unfulfilled:
                print(f"- {task.workname} (срок: {task.deadline})")
        else:
            print("Все задачи выполнены!")

Manager = TaskManager()
Manager.add_task("Подготовить отчет", "2024-04-05")
Manager.add_task("Созвониться с клиентом", "2024-04-10")
Manager.list_unfulfilled()
Manager.mark_completion("Подготовить отчет")
Manager.list_unfulfilled()

