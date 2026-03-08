  # AI Agent (Gemini Function
  Calling)

  A terminal-based AI coding agent
  powered by **Gemini 2.5 Flash**.
  It can inspect files, read
  content, write updates, and
  execute Python scripts through
  tool/function calls.

  ## Features

  - List files and directories
  - Read file contents
  - Write/overwrite files
  - Execute Python files with
  optional arguments
  - Path safety checks to keep
  operations inside an allowed
  working directory

  ## How It Works

  The agent uses Gemini tool
  calling to select and run local
  functions.
  Each function receives a server-
  injected `working_directory`,
  and path validation prevents
  access outside that scope.

  ## Project Structure

  - `main.py` - CLI entrypoint and
  Gemini loop
  - `call_function.py` - Tool
  registry + function dispatch
  - `functions/` - Tool
  implementations:
    - `get_files_info.py`
    - `get_file_content.py`
    - `file_write.py`
    - `run_python_file.py`
  - `prompts.py` - System prompt
  - `calculator/` - Sandbox
  workspace used by tools

  ## Setup

  1. Create a virtual environment
  and install dependencies.
  2. Add your API key to `.env`:

  ```env
  GEMINI_API_KEY=your_api_key_here

  3. Run:

  python main.py "Your prompt
  here"

  Optional verbose mode:

  python main.py "Your prompt
  here" --verbose

  ## Safety Notes

  - File operations are restricted
    to the configured working
    directory.
  - Attempts to access paths
    outside that directory are
    rejected.

  ## Future Improvements

  - Better error handling and
    structured logging
  - More tools (search, patching,
    test runner)
  - Streaming responses and
    improved CLI UX
  - Configurable workspace root
    via CLI/env


  
