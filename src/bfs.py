from .state import State

class BreadthFirstSearch():
    def __init__(self, automated_planning):
        self.visited = []
        self.automated_planning = automated_planning
        self.init = State(self.automated_planning.initial_state)
        self.queue = [self.init]
    
    def search(self):
        while self.queue:
            current_state = self.queue.pop(0)
            if current_state not in self.visited:
                self.visited.append(current_state)

                if self.automated_planning.satisfies(self.automated_planning.problem.goal, current_state.description):
                    return current_state
                
                actions = self.automated_planning.available_actions(current_state.description)
                for act in actions:
                    child = State(description=self.automated_planning.transition(current_state.description, act), parent_action=act, parent=current_state)
                    if child in self.visited:
                        continue
                    self.queue.append(child)
        print("-/!\- No path found -/!\-")
        return []
