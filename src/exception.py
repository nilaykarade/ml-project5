import sys

def error_message_detail(error,error_detail:sys):
    print("error_message_detail------")
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no=str(exc_tb.tb_lineno)

    error_message="Error occured in python script===>"+file_name+"\n Line no.===>"+line_no+"\nError===>"+str(error)

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        print("CustomException-----------------")
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
"""if __name__=="__main__":
    print("main-----------")
    try:
        a=1/0
        print("try-------------")
    except Exception as e:
        #logging.info("Dived by zero...")
        raise CustomException(e,sys)"""
