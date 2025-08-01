import sys


class CustomException(Exception):
    
    def __init__(self, error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = self.get_detail_error(error_msg, error_detail)
    
    @staticmethod
    def get_detail_error(erro_msg,error_detail:sys):
        
        _, _, exc_info = error_detail.exc_info()
        line_no = exc_info.tb_lineno
        file_name = exc_info.tb_frame.f_code.co_filename
        return f"Error in line {line_no} of file {file_name} : {erro_msg}"
    
    def __str__(self):
        return self.error_msg