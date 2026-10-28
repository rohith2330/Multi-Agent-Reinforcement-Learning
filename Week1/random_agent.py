import random

from grid_world import GridWorld


def run_episode(world, max_steps=100):

    world.reset()

    total_reward = 0

    for step in range(max_steps):

        action = random.choice(world.get_actions())

        position, reward, done = world.step(action)

        total_reward += reward

        print(
            f"Step: {step + 1:3d} | "
            f"Action: {action:5s} | "
            f"Position: {position} | "
            f"Reward: {reward}"
        )

        world.render()

        if done:
            print("Goal reached!")
            print("Steps taken:", step + 1)
            print("Total reward:", round(total_reward, 2))
            return True, step + 1, total_reward

    print("Episode ended without reaching the goal.")

    return False, max_steps, total_reward


if __name__ == "__main__":

    random.seed(42)

    world = GridWorld()

    run_episode(world,10)