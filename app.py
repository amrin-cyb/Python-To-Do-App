from storage import load_tasks, save_tasks
import todo


def menu():
    print("------------ This is a to do list ------------")
    print("1. View List")
    print("2. Add List")
    print("3. Mark List as Done")
    print("4. Remove from List")
    print("5. Remove All from List")
    print("6. Find task in List")
    print("7. Update tasks in List")
    print("8. Quit")


def ask_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid number")
        return None


def main():
    tasks = load_tasks()  # load saved tasks when starting

    while True:
        menu()
        choose = input("Choose what to modify: ").strip()

        if choose == "1":
            todo.view(tasks)

        elif choose == "2":
            title = input("Add task: ")
            if todo.add(tasks, title):
                save_tasks(tasks)

        elif choose == "3":
            todo.view(tasks)
            num = ask_int("Choose which task to mark: ")
            if num is not None and todo.mark_done(tasks, num):
                save_tasks(tasks)

        elif choose == "4":
            todo.view(tasks)
            num = ask_int("Choose a task to be removed: ")
            if num is not None and todo.remove(tasks, num):
                save_tasks(tasks)

        elif choose == "5":
            ans = input("Are you sure you want to remove all task? [Y/N]: ")
            if todo.remove_all(tasks, ans):
                save_tasks(tasks)

        elif choose == "6":
            search = input("Search task: ")
            todo.find(tasks, search)

        elif choose == "7":
            todo.view(tasks)
            num = ask_int("Choose which task to change: ")
            if num is None:
                continue
            new_title = input("Enter what to change (leave blank to cancel): ")
            if todo.update(tasks, num, new_title):
                save_tasks(tasks)

        elif choose == "8":
            print("Bye!")
            break

        else:
            print("Please choose a number between 1 to 8")


if __name__ == "__main__":
    main()
