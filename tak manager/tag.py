class Tag:
    """Тег для группировки задач."""

    def __init__(self, name):
        name = name.strip().lower()
        if not name:
            raise ValueError("Название тега не может быть пустым.")
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"#{self._name}"
