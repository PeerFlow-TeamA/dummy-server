
class Env_loader():

    def __init__(self) -> None:
        self.__env = {}
        pass

    def set_env(self, key : str, value : str):
        self.__env[key] = value
    
    def get_env(self, key : str):
        return self.__env[key]

env = Env_loader()
env.set_env("error_msg_key", "message")
env.set_env("category_limit", ["minishell", "ft_irc", "minirt"])
env.set_env("sort_limit", ["lastest", "views", "recommends"])

export = {
    "env": env
}