
class Env_loader():

    def __init__(self) -> None:
        self.__env = {}
        pass

    def set(self, key : str, value : str):
        self.__env[key] = value
    
    def get(self, key : str):
        return self.__env[key]

env = Env_loader()
env.set("error_msg_key", "message")
env.set("category_limit", ["minishell", "ft_irc", "minirt"])
env.set("sort_limit", ["lastest", "views", "recommends"])
env.set("resource_dir", "./resource/")
env.set("question_csv", "question_data.csv")
env.set("answer_csv", "answer_data.csv")
env.set("question_comment_csv", "question_comment_data.csv")
env.set("answer_comment_csv", "answer_comment_data.csv")
env.set("writter_csv", "writter_data.csv")

export = {
    "env": env
}