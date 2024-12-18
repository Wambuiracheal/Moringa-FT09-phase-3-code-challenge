class Magazine:
    def __init__(self, id, name, category=None):
        self._id = id
        self._name = name
        self._category = category or "General"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must not be empty.")

    def __repr__(self):
        return f'<Magazine {self.name}>'
