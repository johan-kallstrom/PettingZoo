---
actions: "Discrete"
title: "Simple Adversary"
agents: "3"
manual-control: "No"
action-shape: "(5)"
action-values: "Discrete(5)"
observation-shape: "(8),(10)"
observation-values: "(-inf,inf)"
import: "pettingzoo.mpe.simple_adversary_v0"
agent-labels: "agents= [adversary_0, agent_0,agent_1]"
---

{% include info_box.md %}



In this environment, there is 1 adversary (red), N good agents (green), N landmarks (default N=2). All agents observe the position of landmarks and other agents. One landmark is the ‘target landmark’ (colored green). Good agents are rewarded based on how close the closest one of them is to the target landmark, but negatively rewarded based on how close the adversary is to the target landmark. The adversary is rewarded based on distance to the target, but it doesn’t know which landmark is the target landmark. All rewards are unscaled Euclidian distance (see main MPE documentation for average distance). This means good agents have to learn to ‘split up’ and cover all landmarks to deceive the adversary.

Agent observation space: `[self_pos, self_vel, goal_rel_position, landmark_rel_position, other_agent_rel_positions]`

Adversary observation space: `[landmark_rel_position, other_agents_rel_positions]`

Agent action space: `[no_action, move_left, move_right, move_down, move_up]`

Adversary action space: `[no_action, move_left, move_right, move_down, move_up]`

### Arguments

```
simple_adversary.env(seed=None, N=2, max_frames=100)
```

`seed`:  seed for random values. Set to None to use machine random source. Set to fixed value for deterministic behavior

`N`:  number of good agents and landmarks

`max_frames`:  number of frames (a step for each agent) until game terminates

