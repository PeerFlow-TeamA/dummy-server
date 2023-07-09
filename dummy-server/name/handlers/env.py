
class Env_loader():

    def __init__(self) -> None:
        self.__env = {}
        pass

    def set(self, key : str, value : str):
        self.__env[key] = value
    
    def get(self, key : str):
        return self.__env[key]

env = Env_loader()

export = {
    "env": env
}