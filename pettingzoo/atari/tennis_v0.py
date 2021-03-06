from pettingzoo.utils.error import DeprecatedEnv


def env(*args, **kwargs):
    raise DeprecatedEnv("tennis_v0 is now depreciated, use tennis_v1 instead")


raw_env = env
parallel_env = env
manual_control = env
