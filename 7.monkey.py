from collections import deque

class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_position = "ground"  # The monkey starts on the ground
        self.banana_position = "hanging"  # The banana is hanging
        self.box_position = "ground"  # The box is on the ground

    def apply_action(self, state, action):
        """Returns new state after performing the action (moving or using the box)"""
        monkey_pos, box_pos, banana_pos = state

        if action == "move_box_under_banana" and box_pos == "ground":
            box_pos = "under_banana"  # Move the box under the banana
        elif action == "monkey_climb_box" and box_pos == "under_banana" and monkey_pos == "ground":
            monkey_pos = "on_box"  # Monkey climbs onto the box
        elif action == "reach_banana" and monkey_pos == "on_box":
            banana_pos = "picked"  # Monkey reaches the banana
            return "Goal"  # Goal state reached

        return (monkey_pos, box_pos, banana_pos)

    def bfs(self):
        """Breadth-First Search to solve the problem"""
        initial_state = ("ground", "ground", "hanging")  # Initial state
        queue = deque([initial_state])
        visited = set([initial_state])

        # Print the initial state
        print(f"Initial State: {initial_state}")

        while queue:
            state = queue.popleft()

            # If the state is the goal
            if state == "Goal":
                print("Goal reached! Monkey got the bananas.")
                return True

            monkey_pos, box_pos, banana_pos = state  # Unpack the state

            # Explore possible actions
            for action in ["move_box_under_banana", "monkey_climb_box", "reach_banana"]:
                new_state = self.apply_action(state, action)

                # If the state changes and hasn't been visited yet, add it to the queue
                if new_state != state and new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)

                    # Output the action and the resulting new state
                    print(f"Move: {action} -> State: {new_state}")

        print("No solution found!")
        return False

# Run the BFS to solve the Monkey and Banana problem
problem = MonkeyBananaProblem()
problem.bfs()