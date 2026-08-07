def main():
    name=None
    while True:
     print("===DEVQUEST===")
     print("1.Create Player")
     print("2.View Player")
     print("3.Exit")
     choice=input("\nChoose an option: ").strip()
     if choice=="1":
          name=create_player()
     elif choice=="2":
          if name is not None:
              view_player(name)
          else:
             print("Create a player first!\n")
     elif choice=="3":
         exit_program()
         break
     else:
         print("\nInvalid option. Please try again.")
         print("\nPress Enter to continue.....")
         input()


def create_player():
    name=input("\nEnter your player name: ")
    print("\nPlayer created successfully!")
    print(f"Welcome {name}. Your adventure begins.")
    print("\nPress enter to continue.....")
    input()
    return name


def view_player(name):
    print("\n===Player Profile===")
    print("Name:",name)
    print("\nPress Enter to continue.....")
    input()


def exit_program():
    print("\nThanks for playing DevQuest!")
    print("Exiting game.....")
    print("Click Enter to Confirm Exit.")
    input()

main()

