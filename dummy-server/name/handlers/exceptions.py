error_msg_key = "message"
sort_value_error_msg = "sort standard incorrected - sort standard must be one of [lastest, views, recommends]"
category_value_error_msg = "category not correct - category must be one of [ft_irc, minishell, minirt]"
question_not_found_error_msg = "Question not found"
password_incorrect_error_msg = "Password incorrect"

class SortValueError(Exception):
    def __init__(self):
        self.message = sort_value_error_msg
    def __str__(self):
        return self.message
    
class CategoryValueError(Exception):
    def __init__(self):
        self.message = category_value_error_msg
    def __str__(self):
        return self.message
    
class QuestionNotFoundError(Exception):
    def __init__(self):
        self.message = question_not_found_error_msg
    def __str__(self):
        return self.message
    
class PasswordIncorrectError(Exception):
    def __init__(self):
        self.message = password_incorrect_error_msg
    def __str__(self):
        return self.message