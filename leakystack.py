# All code in this file is written by William Brown.

# The code written by William Brown in this file is licensed under the Creative Commons
# Attribution-ShareAlike 3.0 Unported License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/
# or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.


class EmptyStack(Exception):
    """
    This exception is raised by the LeakyStack class if the stack is empty and either pop() or top() were called.
    """
    pass


class LeakyStack:
    __doc__ = """A implementation of a leaky stack written by William Brown"""

    def __init__(self, maxelements, listsize=0):
        """
        Initialise the class

        :param int maxelements: The maximum number of elements allowed to be stored in the leaky stack.
        :param int listsize:
        The size of the list which stores the values in the stack. If the value is less than maxelements,
        then listsize will be changed to maxelements. This is to ensure that the list storing the stack
        can fit the stack.
        """
        if listsize < maxelements:  # If the maximum number of elements to be stored is less than the list size, then:
            listsize = maxelements  # Set the list size equal to the maximum number of elements which can be stored
        self._list = [None] * listsize  # Create the list with listsize many None values
        self._maxelements = maxelements  # _maxelements stores the maximum number of values allowed in the leaky stack
        self._listsize = listsize  # _listsize contains the size of the list
        self._start = 0  # _start contains the index of the first value stored
        self._end = 0  # _end contains the index of the last value in the list plus 1, except if the list is empty,
        # when it is the same as the start variable

    def _change_location_variable(self, var, add=1):
        """
        This internal method changes a index by incrementing or decrementing it by the value provided.
        It also ensures that the returned index will not be greater than the size of the list or less than zero.

        :param int var: The index value which needs to be changed
        :param int add: The number to be added (or subtracted if the value is negative) to the index.
        It will be appropriately scaled down if the value is greater than _listsize. The default value is 1.
        :return: The new index to be stored in the appropriate variable
        :rtype: int
        """
        if add > self._listsize != 0:  # If the add is larger than the _listsize (and _listsize is not zero which
            # prevents division by zero errors), then:
            add = add % self._listsize  # Set add equal to the remainder, which is the scaled down value
        if var + add >= self._listsize:  # If the variable + add is larger than the size of the list:
            return (var + add) - self._listsize  # Subtract (var + add) by _listsize to get the correct index
        elif var + add < 0:  # If the variable + add is less than zero:
            return (var + add) + self._listsize  # Add (var + add) and _listsize to get the correct index
        else:  # Otherwise:
            return var + add  # return var + add (the new value of the variable)

    def __len__(self):
        """
        Return the length of the leaky stack

        :return: The length of the leaky stack
        :rtype: int
        """
        if self._end - self._start < 0:  # If the _start index is greater than the _end index:
            return self._end + (self._listsize - self._start)  # Return the number of values from the start of the
            # stack to the end of the list, added with the number of values from the start of the list to the end of
            # the stack.
        else:
            return self._end - self._start  # Subtract _end and _start to get the number of elements in the list

    def push(self, newelement):
        """
        Push an element to the end of the stack, leaking the first value if the stack was full at the time of the push.

        :param newelement: The new element to be pushed into the stack
        """
        if len(self) >= self._maxelements:  # If the stack is full, then:
            print("reached stack limit, so forgot the value " + str(self._list[self._start]))  # Print to the
            # console to say we are leaking the first element in the stack
            self._list[self._start] = None  # Delete the first value in the stack
            self._start = self._change_location_variable(self._start)  # Increment the _start variable as the
            # first value has been leaked
        self._list[self._end] = newelement  # Add the value provided to the end of the stack
        self._end = self._change_location_variable(self._end)  # Increment the end variable as a value has been
        # added to the stack

    def pop(self):
        """
        Pop the element at the top of the stack. This returns the value and removes it from the stack.

        :return: The element currently at the top of the stack.
        """
        if self.is_empty():  # If the stack is empty, then:
            raise EmptyStack("Stack is empty")  # raise an EmptyStack error
        else:  # if it is not empty, then:
            returnvalue = self._list[self._end - 1]  # Assign the first item in the stack to a temporary variable
            self._list[self._end - 1] = None  # Delete the first item in the stack
            self._end = self._change_location_variable(self._end, -1)  # Decrement the _end variable due to the deletion
            return returnvalue  # Now return the value which used to be the first in the stack.

    def is_empty(self):
        """
        Check if the stack is empty. If it is empty return True, if it is not empty return False.

        :return: True if the stack is empty, False otherwise
        :rtype: bool
        """
        if len(self) == 0:  # If the stack is empty, then:
            return True  # return True
        return False  # otherwise, return False

    def top(self):
        """
        Return the value at the top of the stack.

        :return: The element currently at the top of the stack
        """
        if self.is_empty():  # If the stack is empty, then:
            raise EmptyStack("Stack is empty")  # raise an EmptyStack error
        else:  # or if it is not empty, then:
            return self._list[self._start]  # return the first value in the stack.
