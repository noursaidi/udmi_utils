from dataclasses import dataclass

@dataclass
class Error:
    message: str
    schema: str
  
    def __repr__(self):
        return self.message