# To create custom exceptions like when we divide any number by 0 in python we get exception dividing by zero
import traceback
import sys # system library

class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys): # creating constructor
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message,error_detail)

    @staticmethod
    def get_detailed_error_message(error_message , error_detail:sys):

        _, _, exc_tb = traceback.sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename # in which file error occurred
        line_number = exc_tb.tb_lineno                 # in which line error occurred

        return f"Error in {file_name} , line {line_number} : {error_message}"
    
    def __str__(self):
        return self.error_message