import os
from google.genai import types
def write_file(working_directory, file_path, content):
    try:
        abs_work_dir=os.path.abspath(working_directory)
        abs_file_path= os.path.normpath(os.path.join(abs_work_dir,file_path))
        same_path_chk= os.path.commonpath([abs_work_dir,abs_file_path]) == abs_work_dir
        if same_path_chk == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        parent_path= os.path.dirname(abs_file_path)
        os.makedirs(parent_path,exist_ok=True)
        
        with open(abs_file_path,"w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error:{e}"
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite the files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file you have to write to",

            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content that will be written to the file"
            )
        
        },
        required=["file_path","content"]
    ),
)
    
