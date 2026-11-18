from datetime import date, timedelta


def parse_date(text):
    """Превращает строку ГГГГ-ММ-ДД в дату или выбрасывает ValueError."""
    try:
        return date.fromisoformat(text.strip())
    except ValueError:
        raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД, например 2026-11-20.")


class Task:
    """Обычная задача. Базовый класс для остальных видов задач."""

    MIN_PRIORITY = 1
    MAX_PRIORITY = 3

    def __init__(self, title, priority, deadline, tag):
        self._title = self.check_title(title)
        self._priority = self.check_priority(priority)
        self._deadline = deadline
        self._tag = tag
        self._done = False

    #проверки (используются и в main для повторного ввода)
    @staticmethod
    def check_title(title):
        title = title.strip()
        if not title:
            raise ValueError("Название задачи не может быть пустым.")
        return title

    @classmethod
    def check_priority(cls, value):
        if not isinstance(value, int) or not cls.MIN_PRIORITY <= value <= cls.MAX_PRIORITY:
            raise ValueError(
                f"Приоритет должен быть целым числом от {cls.MIN_PRIORITY} до {cls.MAX_PRIORITY}."
            )
        return value

    #свойства
    @property
    def title(self):
        return self._title

    @property
    def priority(self):
        return self._priority

    @property
    def deadline(self):
        return self._deadline

    @property
    def tag(self):
        return self._tag

    @property
    def done(self):
        return self._done

    #поведение
    def mark_done(self):
        if self._done:
            raise ValueError(f"Задача «{self._title}» уже выполнена.")
        self._done = True

    def is_overdue(self, today):
        return not self._done and self._deadline < today

    def describe(self):
        """Описание задачи. Переопределяется в наследниках (полиморфизм)."""
        return f"{self._title} | приоритет {self._priority} | до {self._deadline} | {self._tag}"

    def __str__(self):
        mark = "x" if self._done else " "
        return f"[{mark}] {self.describe()}"


class UrgentTask(Task):
    """Срочная задача: приоритет всегда 1, в описании есть пометка."""

    def __init__(self, title, deadline, tag):
        super().__init__(title, Task.MIN_PRIORITY, deadline, tag)

    def describe(self):
        return "СРОЧНО! " + super().describe()


class RecurringTask(Task):
    """Повторяющаяся задача: при выполнении срок переносится вперёд."""

    def __init__(self, title, priority, deadline, tag, every_days):
        super().__init__(title, priority, deadline, tag)
        self._every_days = self.check_days(every_days)

    @staticmethod
    def check_days(value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Период повтора должен быть целым числом дней, не меньше 1.")
        return value

    @property
    def every_days(self):
        return self._every_days

    def mark_done(self):
        # не закрываем задачу, а переносим срок на следующий период
        self._deadline = self._deadline + timedelta(days=self._every_days)

    def describe(self):
        return super().describe() + f" | повтор каждые {self._every_days} дн."
