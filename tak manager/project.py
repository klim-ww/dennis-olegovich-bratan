class Project:
    """Проект хранит свой список задач."""

    def __init__(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Название проекта не может быть пустым.")
        self._name = name
        self._tasks = []

    @property
    def name(self):
        return self._name

    @property
    def tasks(self):
        return list(self._tasks)  # копия, чтобы список нельзя было испортить снаружи

    def find_task(self, title):
        for task in self._tasks:
            if task.title.lower() == title.strip().lower():
                return task
        return None

    def add_task(self, task):
        if self.find_task(task.title) is not None:
            raise ValueError(f"Задача «{task.title}» уже есть в проекте «{self._name}».")
        self._tasks.append(task)

    def remove_task(self, task):
        self._tasks.remove(task)

    def __len__(self):
        return len(self._tasks)

    def __str__(self):
        return f"Проект «{self._name}» (задач: {len(self._tasks)})"
