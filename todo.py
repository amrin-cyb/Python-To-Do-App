def view(tasks):
    if not tasks:
        print("There is no task to do")
        return

    for i, t in enumerate(tasks, start=1):
        status = "[DONE]" if t["done"] else "[]"
        print(f"{i}. {status} {t['title']}")


def add(tasks, title):
    title = title.strip()
    if not title:
        print("Please enter something")
        return False

    for t in tasks:
        if t["title"].lower() == title.lower():
            print("This task already exists")
            return False

    tasks.append({"title": title, "done": False})
    print(f"{title} added")
    return True


def mark_done(tasks, num):
    if not tasks:
        print("There is no task to mark")
        return False

    if 1 <= num <= len(tasks):
        tasks[num - 1]["done"] = True
        print(f"{tasks[num - 1]['title']} marked as done")
        return True

    print("Choose a number within the tasks")
    return False


def remove(tasks, num):
    if not tasks:
        print("There is no task to be removed")
        return False

    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        print(f"{removed['title']} removed")
        return True

    print("Choose a number within the tasks")
    return False


def remove_all(tasks, answer):
    if not tasks:
        print("There is no task to be removed")
        return False

    answer = answer.strip().lower()
    if answer == "y":
        tasks.clear()
        print("All tasks removed")
        return True
    elif answer == "n":
        print("Tasks not removed")
        return False

    print("Invalid answer choose Y/N only")
    return False


def find(tasks, search):
    search = search.strip().lower()
    if not search:
        print("Please enter something to search")
        return

    found = []
    for t in tasks:
        if search in t["title"].lower():
            found.append(t)

    if not found:
        print(f"{search} not found")
        return

    for t in found:
        status = "[DONE]" if t["done"] else "[]"
        print(f"{status} {t['title']} found")


def update(tasks, num, new_title):
    if not tasks:
        print("There is no task to change")
        return False

    if not (1 <= num <= len(tasks)):
        print("Choose a number within the tasks")
        return False

    new_title = new_title.strip()
    if not new_title:
        print("None changed")
        return False

    # prevent duplicates
    for i, t in enumerate(tasks):
        if i != num - 1 and t["title"].lower() == new_title.lower():
            print("Another task already has that title")
            return False

    tasks[num - 1]["title"] = new_title
    print("Task changed")
    return True
