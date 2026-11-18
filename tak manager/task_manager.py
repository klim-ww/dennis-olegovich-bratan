from project import Project
from tag import Tag


class TaskManager:
    """Главный класс: содержит проекты, теги и задачи (композиция)."""

    def __init__(self):
        self._projects = {}
        self._tags = {}

    @property
    def projects(self):
        return list(self._projects.values())

    def get_tag(self, tag_name):
        """Находит тег или создаёт новый."""
        key = tag_name.strip().lower()
        if key not in self._tags:
            self._tags[key] = Tag(key)
        return self._tags[key]

    def all_tasks(self):
        result = []
        for project in self._projects.values():
            result.extend(project.tasks)
        return result

    def find_task(self, title):
        for project in self._projects.values():
            task = project.find_task(title)
            if task is not None:
                return task
        return None

    def add_task(self, project_name, task):
        if self.find_task(task.title) is not None:
            raise ValueError(f"Задача «{task.title}» уже существует.")
        key = project_name.strip()
        if key not in self._projects:
            self._projects[key] = Project(key)
        self._projects[key].add_task(task)

    def complete_task(self, title):
        task = self.find_task(title)
        if task is None:
            raise ValueError(f"Задача «{title}» не найдена.")
        task.mark_done()
        return task

    def delete_task(self, title):
        for project in self._projects.values():
            task = project.find_task(title)
            if task is not None:
                project.remove_task(task)
                return task
        raise ValueError(f"Задача «{title}» не найдена.")

    def filter_by_tag(self, tag_name):
        key = tag_name.strip().lower()
        return [task for task in self.all_tasks() if task.tag.name == key]

    def overdue_tasks(self, today):
        return [task for task in self.all_tasks() if task.is_overdue(today)]

    def sorted_by_priority(self):
        return sorted(self.all_tasks(), key=lambda task: (task.priority, task.deadline))

    def __str__(self):
        return f"TaskManager: проектов {len(self._projects)}, задач {len(self.all_tasks())}"
