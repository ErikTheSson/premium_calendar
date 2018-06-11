import enum

from IdeaManager import StorageManager
# TODO NEXT: PROJECT MANAGER

def main():
    smanager = StorageManager()
    StorageManager.new_item(smanager, "first entry")
    print("my list is \n%s" % StorageManager.__repr__(smanager))


if __name__ == '__main__':
    main()