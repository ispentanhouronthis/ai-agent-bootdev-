from google.genai import types
import os
def get_file_content(working_directory, file_path):
    try:
            
        abs_work_dir=os.path.abspath(working_directory)
        abs_file_path=os.path.normpath(os.path.join(abs_work_dir,file_path))
        valid_path_chk= os.path.commonpath([abs_file_path,abs_work_dir]) == abs_work_dir
        if valid_path_chk == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(abs_file_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        MAX_CHARS=10000
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        print(f"Error:{e}")
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="read the file contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read",
            ),
            
        },
        required=["file_path"]

    ),
)  
