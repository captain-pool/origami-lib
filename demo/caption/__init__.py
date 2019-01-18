import os
PATH = os.path.dirname(os.path.abspath(__file__))
if os.name.lower() != 'posix':
    raise OSError("Download cocoapi from https://github.com/cocodataset/cocoapi.git and place it in %s. The folder name must be 'cocoapi'. Follow README and build the PythonAPI"%PATH)
else:
    os.system("sh "+os.path.join(PATH,"get_cocoapi.sh"))
