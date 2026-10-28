import random

# Grid symbols
EMPTY = "."
OBSTACLE = "#"
START = "S"
GOAL = "G"
AGENT = "R"


class GridWorld:

    def __init__(self, size=6):
        self.size = size

        self.start = (2, 0)
        self.goal = (5, 5)

        self.obstacles = {
            (1, 1),
            (1, 2),
            (2, 2),
            (3, 4),
            (4, 1),
        }

        self.position = self.start
        self.steps = 0

    def reset(self):
        """Reset the environment for a new episode."""
        self.position = self.start
        self.steps = 0

        return self.position

    def get_actions(self):
        """Return the four possible movement actions."""
        return ["UP", "DOWN", "LEFT", "RIGHT"]

    def step(self, action):
        """Execute an action and update the environment."""

        row, col = self.position

        if action == "UP":
            row -= 1
        elif action == "DOWN":
            row += 1
        elif action == "LEFT":
            col -= 1
        elif action == "RIGHT":
            col += 1
        else:
            raise ValueError(f"Invalid action: {action}")

        # Check grid boundaries.
        if not (0 <= row < self.size and
                0 <= col < self.size):
            return self.position, -1, False

        next_position = (row, col)

        # Prevent movement into obstacles.
        if next_position in self.obstacles:
            return self.position, -1, False

        self.position = next_position
        self.steps += 1

        # Reaching the goal ends the episode.
        if self.position == self.goal:
            return self.position, 10, True

        return self.position, -0.1, False

    def render(self):
        """Print the current state of the grid."""

        for row in range(self.size):
            cells = []

            for col in range(self.size):
                position = (row, col)

                if position == self.position:
                    cells.append(AGENT)
                elif position == self.start:
                    cells.append(START)
                elif position == self.goal:
                    cells.append(GOAL)
                elif position in self.obstacles:
                    cells.append(OBSTACLE)
                else:
                    cells.append(EMPTY)

            print(" ".join(cells))

        print()


if __name__ == "__main__":

    world = GridWorld()

    world.render()

    print("Initial position:", world.position)
    print("Goal position:", world.goal)
    print("Available actions:", world.get_actions())