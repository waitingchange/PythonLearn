class parent(object):
    def __init__(self):
        self._name = None
        self._age = None
        print 'parent is init'

    def run(self):
        print 'parent run ', self._name


class child(parent):
    def __init__(self):
        super(child, self).__init__()
        print 'child is init'

    def run(self):
        print 'child run'






