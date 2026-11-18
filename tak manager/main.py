from datetime import date

from task import RecurringTask, Task, UrgentTask, parse_date
from task_manager import TaskManager

HELP_TEXT = """Команды:
  help     - список команд
  add      - добавить задачу (обычная / срочная / повторяющаяся)
  list     - показать все задачи
  projects - показать проекты
  tag      - показать задачи по тегу
  overdue  - показать просроченные задачи
  sort     - показать задачи по приоритету
  done     - отметить задачу выполненной
  delete   - удалить задачу
  demo     - загрузить примеры задач
  exit     - выход"""


#ввод с повтором при ошибке
def ask(prompt, convert=str):
    while True:
        raw = input(prompt).strip()
        try:
            return convert(raw)
        except ValueError as error:
            print(f"Ошибка: {error}")


def non_empty(text):
    if not text:
        raise ValueError("Поле не может быть пустым.")
    return text


def to_priority(text):
    try:
        return Task.check_priority(int(text))
    except ValueError:
        raise ValueError(
            f"Приоритет должен быть целым числом от {Task.MIN_PRIORITY} до {Task.MAX_PRIORITY}."
        )


def to_days(text):
    try:
        return RecurringTask.check_days(int(text))
    except ValueError:
        raise ValueError("Период повтора должен быть целым числом дней, не меньше 1.")


def to_kind(text):
    if text not in ("1", "2", "3"):
        raise ValueError("Введите 1, 2 или 3.")
    return text


def to_date_or_today(text):
    return date.today() if text == "" else parse_date(text)


def show_list(title, tasks):
    print(f"\n--- {title} ---")
    if not tasks:
        print("(пусто)")
    for task in tasks:
        print(task)

#команды
def cmd_help(manager):
    print(HELP_TEXT)


def cmd_add(manager):
    kind = ask("Тип (1 - обычная, 2 - срочная, 3 - повторяющаяся): ", to_kind)
    project = ask("Проект: ", non_empty)
    title = ask("Название: ", Task.check_title)
    tag = manager.get_tag(ask("Тег: ", non_empty))
    deadline = ask("Срок (ГГГГ-ММ-ДД): ", parse_date)

    if kind == "2":
        task = UrgentTask(title, deadline, tag)
    else:
        priority = ask("Приоритет (1 - высокий ... 3 - низкий): ", to_priority)
        if kind == "3":
            days = ask("Повтор каждые N дней: ", to_days)
            task = RecurringTask(title, priority, deadline, tag, days)
        else:
            task = Task(title, priority, deadline, tag)

    manager.add_task(project, task)
    print("Добавлено:", task)


def cmd_list(manager):
    show_list("Все задачи", manager.all_tasks())


def cmd_projects(manager):
    print("\n--- Проекты ---")
    if not manager.projects:
        print("(пусто)")
    for project in manager.projects:
        print(project)


def cmd_tag(manager):
    name = ask("Тег: ", non_empty)
    show_list(f"Задачи с тегом '{name}'", manager.filter_by_tag(name))


def cmd_overdue(manager):
    today = ask("Дата (Enter - сегодня): ", to_date_or_today)
    show_list(f"Просроченные на {today}", manager.overdue_tasks(today))


def cmd_sort(manager):
    show_list("По приоритету", manager.sorted_by_priority())


def cmd_done(manager):
    task = manager.complete_task(ask("Название задачи: ", non_empty))
    if task.done:
        print("Выполнено:", task)
    else:
        print("Повторяющаяся задача, срок перенесён:", task)


def cmd_delete(manager):
    task = manager.delete_task(ask("Название задачи: ", non_empty))
    print("Удалено:", task.title)


def cmd_demo(manager):
    samples = [
        ("Учёба", Task("Сделать лабораторную", 1, parse_date("2026-11-20"), manager.get_tag("универ"))),
        ("Учёба", Task("Выучить Python", 2, parse_date("2026-11-10"), manager.get_tag("универ"))),
        ("Учёба", UrgentTask("Сдать физкультуру", parse_date("2026-11-05"), manager.get_tag("универ"))),
        ("Дом", Task("Купить продукты", 2, parse_date("2026-11-18"), manager.get_tag("быт"))),
        ("Дом", RecurringTask("Оплатить интернет", 1, parse_date("2026-11-08"), manager.get_tag("быт"), 30)),
    ]
    added = 0
    for project, task in samples:
        try:
            manager.add_task(project, task)
            added += 1
        except ValueError:
            pass  # такая задача уже есть
    print(f"Добавлено примеров: {added}")


COMMANDS = {
    "help": cmd_help,
    "add": cmd_add,
    "list": cmd_list,
    "projects": cmd_projects,
    "tag": cmd_tag,
    "overdue": cmd_overdue,
    "sort": cmd_sort,
    "done": cmd_done,
    "delete": cmd_delete,
    "demo": cmd_demo,
}


def main():
    manager = TaskManager()
    print("Менеджер задач. Введите help, чтобы увидеть команды.")
    while True:
        try:
            command = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nДо свидания!")
            break

        if command == "exit":
            print("До свидания!")
            break

        handler = COMMANDS.get(command)
        if handler is None:
            print("Неизвестная команда. Введите help, чтобы увидеть список команд.")
            continue

        try:
            handler(manager)
        except ValueError as error:
            print(f"Ошибка: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nОперация отменена.")


if __name__ == "__main__":
    main()
