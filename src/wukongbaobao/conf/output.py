import os

def init_output_dir():
    output_dir = os.path.join(os.getcwd(), 'output')
    if os.path.exists(output_dir):
        pass
    else:
        os.mkdir(output_dir)
    
    return output_dir