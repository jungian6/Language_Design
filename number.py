from errors import RTError
from values import Value
from boolean import Boolean


class Number(Value):
    """Number Class"""

    def __init__(self, value):
        super().__init__()
        self.value = value

    def added_to(self, other):
        """Add the number to another number"""
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def subbed_by(self, other):
        """Subtract the number from another number"""
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        """Multiply the number by another number"""
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        """Divide the number by another number"""
        if isinstance(other, Number):
            if other.value == 0:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Division by zero',
                    self.context
                )

            return Number(self.value / other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def power_by(self, other):
        """Raise the number to the power of another number"""
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_eq(self, other):
        """Check if the number is equal to another number"""
        if isinstance(other, Number):
            return Boolean(self.value == other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_ne(self, other):
        """Check if the number is not equal to another number"""
        if isinstance(other, Number):
            return Boolean(self.value != other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lt(self, other):
        """Check if the number is less than another number"""
        if isinstance(other, Number):
            return Boolean(self.value < other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gt(self, other):
        """Check if the number is greater than another number"""
        if isinstance(other, Number):
            return Boolean(self.value > other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lte(self, other):
        """Check if the number is less than or equal to another number"""
        if isinstance(other, Number):
            return Boolean(self.value <= other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gte(self, other):
        """Check if the number is greater than or equal to another number"""
        if isinstance(other, Number):
            return Boolean(self.value >= other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def anded_by(self, other):
        """Check if the number is anded by another number"""
        if isinstance(other, Number):
            return Boolean(self.value and other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def ored_by(self, other):
        """Check if the number is ored by another number"""
        if isinstance(other, Number):
            return Boolean(self.value or other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def notted(self):
        """Check if the number is notted"""
        return Boolean(not self.value).set_context(self.context), None

    def copy(self):
        """Copy the number"""
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.value != 0

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
