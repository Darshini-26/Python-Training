from db1 import Database
from user import User
 
class Logic:
    def __init__(self):
        self.db = Database()
 
    def adduserlogic(self, name, age):
        """Add a user by calling the `adduser` method in `db.py`."""
        user_obj = User(name, age)
        return self.db.adduser(user_obj)
 
    def getalluserlogic(self):
        """Get all users by calling the `getallusers` method in `db.py`."""
        return self.db.getallusers()
 
    def cleanupresources(self):
        """Clean up resources by calling the `cleanup` method in `db.py`."""
        return self.db.cleanup()
 
# Test the logic functions
if __name__ == '__main__':
    logic = Logic()
   
    print("Adding users...")
    if logic.adduserlogic("A", 26):
        print("User A added successfully.")
    if logic.adduserlogic("B", 25):
        print("User B added successfully.")
   
    # Test getalluserlogic
    # print("\nFetching all users...")
    users = logic.getalluserlogic()
    for user in users:
        print(f"Name: {user.name}, Age: {user.age}")
   
    # # Test cleanupresources
    # print("\nCleaning up resources...")
    # if logic.cleanupresources():
    #     print("Cleanup successful.")
   
   
 
   
    