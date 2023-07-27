
def Equals(id1, id2):
    return id1 == id2

#idvalidation       
def IsNotValid(id):
   if len(id) == 0:
     return True
   return False

def user_already_exists():
   return True