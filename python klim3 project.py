
#тег
class Tag:
    def __init__(self, name):
        self.name = name


#задача
class Task:
    def __init__(self, title, priority, deadline, tag):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.tag = tag
        self.done = False

    def mark_done(self):
        self.done = True

    def show(self):
        mark = "x" if self.done else " "
        print(f"[{mark}] {self.title} | приоритет {self.priority} | до {self.deadline} | #{self.tag.name}")


#проект
class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


#TaskManager
class TaskManager:
    def __init__(self):
        self.projects = {}
        self.tags = {}
    #найти тег или создать новый
    def get_tag(self, tag_name):
        if tag_name not in self.tags:
            self.tags[tag_name] = Tag(tag_name)
        return self.tags[tag_name]

    #собрать все задачи из всех проектов в один список
    def all_tasks(self):
        result = []
        for project in self.projects.values():
            for task in project.tasks:
                result.append(task)
        return result

    #добавить задачу
    def add_task(self, project_name, title, priority, deadline, tag_name):
        if project_name not in self.projects:
            self.projects[project_name] = Project(project_name)
        task = Task(title, priority, deadline, self.get_tag(tag_name))
        self.projects[project_name].add_task(task)

    #отметить выполненной
    def complete_task(self, title):
        for task in self.all_tasks():
            if task.title == title:
                task.mark_done()
                return True
        return False              # такой задачи нет

    #фильтр по тегу
    def filter_by_tag(self, tag_name):
        result = []
        for task in self.all_tasks():
            if task.tag.name == tag_name:
                result.append(task)
        return result

    #просроченные
    def overdue_tasks(self, today):
        result = []
        for task in self.all_tasks():
            if not task.done and task.deadline < today:
                result.append(task)
        return result

    #сортировка по приоритету
    def sorted_by_priority(self):
        tasks = self.all_tasks()
        tasks.sort(key=lambda task: task.priority)
        return tasks


#Демонстрация
def show_list(title, tasks):
    print(f"\n--- {title} ---")
    if len(tasks) == 0:
        print("(пусто)")
    for task in tasks:
        task.show()


manager = TaskManager()

# добавляем задачи в два проекта
manager.add_task("Учёба", "Сделать лабораторную", 1, "2026-11-20", "универ")
manager.add_task("Учёба", "Выучить Python", 2, "2026-11-10", "универ")
manager.add_task("Учёба", "Сдать физкультуру", 3, "2026-11-05", "универ")
manager.add_task("Дом", "Купить продукты", 2, "2026-11-18", "быт")
manager.add_task("Дом", "Оплатить интернет", 1, "2026-11-08", "быт")

show_list("Все задачи", manager.all_tasks())

# отмечаем выполненной
print("\nОтметили 'Выучить Python':", manager.complete_task("Выучить Python"))
print("Отметили 'Несуществующая':", manager.complete_task("Несуществующая"))

show_list("Фильтр по тегу 'универ'", manager.filter_by_tag("универ"))
show_list("Просроченные на 2026-11-17", manager.overdue_tasks("2026-11-17"))
show_list("Сортировка по приоритету", manager.sorted_by_priority())
