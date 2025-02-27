import time
from abc import abstractmethod
import warnings

class BaseAPI:
    
    def __init__(self, 
                 retry=5, 
                 wait=5, 
                 system_prompt=None, 
                 verbose=True,
                 fail_msg='Failed to obtain answer via API.',
                 **kwargs):
        self.wait = wait 
        self.retry = retry
        self.system_prompt = system_prompt
        self.kwargs = kwargs
        self.verbose = verbose
        self.fail_msg = fail_msg
        if len(kwargs):
            warnings.warn(f'BaseAPI received the following kwargs: {kwargs}')
            warnings.warn(f'Will try to use them as kwargs for `generate`. ')

    @abstractmethod
    def generate_inner(self, inputs, **kwargs):
        warnings.warn(f'For APIBase, generate_inner is an abstract method. ')
        assert 0, 'generate_inner not defined'
        ret_code, answer, log = None, None, None
        # if ret_code is 0, means succeed
        return ret_code, answer, log

    def generate(self, inputs, **kwargs):
        input_type = None
        if isinstance(inputs, str):
            input_type = 'str'
        elif isinstance(inputs, list) and isinstance(inputs[0], str):
            input_type = 'strlist'
        elif isinstance(inputs, list) and isinstance(inputs[0], dict):
            input_type = 'dictlist'
        assert input_type is not None, input_type

        answer = None
        for i in range(self.retry):
            try:
                ret_code, answer, log = self.generate_inner(inputs, **kwargs)
                if ret_code == 0 and self.fail_msg not in answer and answer != '':
                    return answer
                elif self.verbose:
                    warnings.warn(f"RetCode: {ret_code}\nAnswer: {answer}\nLog: {log}")
            except:
                if self.verbose:
                    warnings.warn(f"An unknown exception occurs during try {i}")
            time.sleep(self.wait)
        return self.fail_msg if answer in ['', None] else answer
        

        