class Stack:
    """Class Stack simulates a tower to hold disks, and larger disks cannot be placed on the top of smller dkiks."""

    def __init__(self, name: str):
        self._stack = []
        self._name = name
    
    def __str__(self) -> str:
        """can easy to print currently disks info"""
        
        return f"stack {self._name}: " + ",".join(map(str, self._stack))

    def __len__(self) -> int:
        """used to len()"""
        
        return len(self._stack)
    
    def push(self, value) -> bool:
        """Push a value to the stack, a new value should less than the top of the stack"""
        
        if (not self._stack) or self._stack[-1] > value:
            self._stack.append(value)
            return True
        
        return False
    
    def pop(self) -> any:
        if (self._stack):
            return self._stack.pop()
        
        return None


def recursive_move(n, src, dest, aux, print_func):
    """n: the number of disks to move,
       src: the disk in the starting stack,
       dest: the disk could be moved to the destination stack,
       aux: a stack used to store the non targetted disk,
       print_func: a function to print all stakcs info"""
       
    if n == 0:
        # indicate there has no disk needed to be moved
        return
    
    # if we want to move a targetted disk, we could remove non-targetted disks to aux frist
    recursive_move(n-1, src, aux, dest, print_func)
    # ok, we just the targetted disk to destination stack
    x = src.pop()
    assert x != None
    r = dest.push(x)
    assert r == True
    print_func()
    # we just move rest disks in the aux stack to destination stack
    recursive_move(n-1, aux, dest, src, print_func)
    

def main():
    stack_a = Stack("SA")
    stack_b = Stack("SB") 
    stack_c = Stack("SC")

    def print_stack():
        """a closure function includes all staks and print their info"""

        nonlocal stack_a, stack_b, stack_c
        print(f"{stack_a}")
        print(f"{stack_b}")
        print(f"{stack_c}")
        print(r"------------------------")
    
    # you can change number of disks, this is from 5 to 1
    for x in range(5, 0, -1):
        stack_a.push(x)
    
    print(r"--------start--------")
    print_stack()
    
    # remove all disks from SA to SC
    recursive_move(len(stack_a), stack_a, stack_c, stack_b, print_stack)
    
    print(r"--------final--------")
    print_stack()

if __name__ == "__main__":
    main()



"""
output result as a reference:

--------start--------
stack SA: 5,4,3,2,1
stack SB:
stack SC:
------------------------
stack SA: 5,4,3,2
stack SB:
stack SC: 1
------------------------
stack SA: 5,4,3
stack SB: 2
stack SC: 1
------------------------
stack SA: 5,4,3
stack SB: 2,1
stack SC:
------------------------
stack SA: 5,4
stack SB: 2,1
stack SC: 3
------------------------
stack SA: 5,4,1
stack SB: 2
stack SC: 3
------------------------
stack SA: 5,4,1
stack SB:
stack SC: 3,2
------------------------
stack SA: 5,4
stack SB:
stack SC: 3,2,1
------------------------
stack SA: 5
stack SB: 4
stack SC: 3,2,1
------------------------
stack SA: 5
stack SB: 4,1
stack SC: 3,2
------------------------
stack SA: 5,2
stack SB: 4,1
stack SC: 3
------------------------
stack SA: 5,2,1
stack SB: 4
stack SC: 3
------------------------
stack SA: 5,2,1
stack SB: 4,3
stack SC:
------------------------
stack SA: 5,2
stack SB: 4,3
stack SC: 1
------------------------
stack SA: 5
stack SB: 4,3,2
stack SC: 1
------------------------
stack SA: 5
stack SB: 4,3,2,1
stack SC:
------------------------
stack SA:
stack SB: 4,3,2,1
stack SC: 5
------------------------
stack SA: 1
stack SB: 4,3,2
stack SC: 5
------------------------
stack SA: 1
stack SB: 4,3
stack SC: 5,2
------------------------
stack SA:
stack SB: 4,3
stack SC: 5,2,1
------------------------
stack SA: 3
stack SB: 4
stack SC: 5,2,1
------------------------
stack SA: 3
stack SB: 4,1
stack SC: 5,2
------------------------
stack SA: 3,2
stack SB: 4,1
stack SC: 5
------------------------
stack SA: 3,2,1
stack SB: 4
stack SC: 5
------------------------
stack SA: 3,2,1
stack SB:
stack SC: 5,4
------------------------
stack SA: 3,2
stack SB:
stack SC: 5,4,1
------------------------
stack SA: 3
stack SB: 2
stack SC: 5,4,1
------------------------
stack SA: 3
stack SB: 2,1
stack SC: 5,4
------------------------
stack SA:
stack SB: 2,1
stack SC: 5,4,3
------------------------
stack SA: 1
stack SB: 2
stack SC: 5,4,3
------------------------
stack SA: 1
stack SB:
stack SC: 5,4,3,2
------------------------
stack SA:
stack SB:
stack SC: 5,4,3,2,1
------------------------
--------final--------
stack SA:
stack SB:
stack SC: 5,4,3,2,1
------------------------
"""