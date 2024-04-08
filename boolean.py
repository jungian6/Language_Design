from values import Value


class Boolean(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def get_comparison_eq(self, other):
        if isinstance(other, Boolean):
            return Boolean(self.value == other.value).set_context(self.context), None
        else:
            return None, self.illegal_operation(other)

    def get_comparison_ne(self, other):
        if isinstance(other, Boolean):
            return Boolean(self.value != other.value).set_context(self.context), None
        else:
            return None, self.illegal_operation(other)

    def anded_by(self, other):
        if isinstance(other, Boolean):
            return Boolean(self.value and other.value).set_context(self.context), None
        else:
            return None, self.illegal_operation(other)

    def ored_by(self, other):
        if isinstance(other, Boolean):
            return Boolean(self.value or other.value).set_context(self.context), None
        else:
            return None, self.illegal_operation(other)

    def notted(self):
        return Boolean(not self.value).set_context(self.context), None

    def copy(self):
        copy = Boolean(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.value

    def __str__(self):
        return "true" if self.value else "false"

    def __repr__(self):
        return str(self.value)