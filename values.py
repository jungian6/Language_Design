from main import *

class Value:
    """Value Class"""

    def __init__(self):
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        """Set the position of the value"""
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        """Set the context of the value"""
        self.context = context
        return self

    def added_to(self, other):
        """Add the value to another value"""
        return None, self.illegal_operation(other)

    def subbed_by(self, other):
        """Subtract the value from another value"""
        return None, self.illegal_operation(other)

    def multed_by(self, other):
        """Multiply the value by another value"""
        return None, self.illegal_operation(other)

    def dived_by(self, other):
        """Divide the value by another value"""
        return None, self.illegal_operation(other)

    def power_by(self, other):
        """Raise the value to the power of another value"""
        return None, self.illegal_operation(other)

    def get_comparison_eq(self, other):
        """Check if the value is equal to another value"""
        return None, self.illegal_operation(other)

    def get_comparison_ne(self, other):
        """Check if the value is not equal to another value"""
        return None, self.illegal_operation(other)

    def get_comparison_lt(self, other):
        """Check if the value is less than another value"""
        return None, self.illegal_operation(other)

    def get_comparison_gt(self, other):
        """Check if the value is greater than another value"""
        return None, self.illegal_operation(other)

    def get_comparison_lte(self, other):
        """Check if the value is less than or equal to another value"""
        return None, self.illegal_operation(other)

    def get_comparison_gte(self, other):
        """Check if the value is greater than or equal to another value"""
        return None, self.illegal_operation(other)

    def anded_by(self, other):
        """Check if the value is anded by another value"""
        return None, self.illegal_operation(other)

    def ored_by(self, other):
        """Check if the value is ored by another value"""
        return None, self.illegal_operation(other)

    def notted(self, other):
        """Check if the value is notted"""
        return None, self.illegal_operation(other)

    def execute(self, args):
        """Execute the value"""
        return RTResult().failure(self.illegal_operation())

    def copy(self):
        """Copy the value"""
        raise Exception('No copy method defined')

    def is_true(self):
        """Check if the value is true"""
        return False

    def illegal_operation(self, other=None):
        """Return an illegal operation error"""
        if not other:
            other = self
        return RTError(
            self.pos_start, other.pos_end,
            'Illegal operation',
            self.context
        )