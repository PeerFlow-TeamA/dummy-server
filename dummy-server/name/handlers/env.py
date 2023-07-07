
class Env_loader():

    def __init__(self) -> None:
        self.__env = {}
        pass

    def set_env(self, key : str, value : str):
        self.__env[key] = value
    
    def get_env(self, key : str):
        return self.__env[key]

env = Env_loader()
env.set_env("title", "minishell")

export = {
    "env": env
}