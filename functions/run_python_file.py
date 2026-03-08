import os
import subprocess
from google.genai import types
def run_python_file(working_directory, file_path, args=None):
    try:
        abs_work_dir=os.path.abspath(working_directory)
        abs_file_path=os.path.normpath(os.path.join(abs_work_dir,file_path))
        valid_path_chk= os.path.commonpath([abs_file_path,abs_work_dir]) == abs_work_dir
        if valid_path_chk == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(abs_file_path) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        str_path= str(abs_file_path)
        if str_path.endswith('.py') == False:
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", abs_file_path]
        if args!=None:
            command.extend(args)
        comp_obj=subprocess.run(command,capture_output=True,text=True,timeout=30)
        rtn_str_list=[]
        if comp_obj.returncode != 0 :
            rtn_str_list.append("Process exited with code X")
        if comp_obj.stdout==None or comp_obj.stderr==None:
            rtn_str_list.append("No output produced")
        else:
            rtn_str_list.append(f"STDOUT:{comp_obj.stdout}\n STDERR:{comp_obj.stderr}")
        return ''.join(rtn_str_list)
    except Exception as e:
        return f"Error: executing Python file: {e}"
schema_run_python_file= types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the python file to execute",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING
                ),
                description="Optional list of arguments to pass to script"
            )
        },
        required=["file_path"]
    ),
) 


