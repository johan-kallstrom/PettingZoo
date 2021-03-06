from ._mpe_utils.simple_env import SimpleEnv, make_env
from .scenarios.simple_crypto import Scenario
from pettingzoo.utils.to_parallel import parallel_wrapper_fn


class raw_env(SimpleEnv):

    def __init__(self, seed=None, max_frames=100):
        scenario = Scenario()
        world = scenario.make_world()
        super().__init__(scenario, world, max_frames, seed)


env = make_env(raw_env)
parallel_env = parallel_wrapper_fn(env)
