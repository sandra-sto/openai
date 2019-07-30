import gym

env = gym.make('Reverse-v0')
env.reset()
print(env.action_space)
print(env.observation_space)

for i in range(10):
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

    print (i)
    print(action)
    print(state)
    print(reward)
    print(done)

    env.render()
    if done:
        break

