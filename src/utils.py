import sys
import io
from contextlib import redirect_stdout

class capture(redirect_stdout):

    def __init__(self):
        self.f = io.StringIO()
        self._new_target = self.f
        self._old_targets = []  # verbatim from parent class

    def __enter__(self):
        self._old_targets.append(getattr(sys, self._stream))  # verbatim from parent class
        setattr(sys, self._stream, self._new_target)  # verbatim from parent class
        return self  # instead of self._new_target in the parent class

    def __repr__(self):
        return self.f.getvalue() 