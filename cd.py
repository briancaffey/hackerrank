# implementing cd in python

class Path:
    def __init__(self, path):
        self.path = path

    def cd(self, p):

        if p[0] == '/' or p == '':
            self.path = p
            return self.path

        changes = p.split('/')

        for i in changes:
            if i == '':
                next
            if i == '..':
                self.path = self.get_parent()
            else:
                self.path = '/'.join(self.path.split('/') + [i])

        return self.path

    def get_parent(self):
        return '/'.join(self.path.split('/')[:-1])

    def current_path(self):
        return self.path


path = Path('/a/b/c/d')
print path.current_path()
path.cd('../x')
print path.current_path()

path1= Path('b/c/d/g')
path1.cd('../../dfddfd')
print path1.current_path()
