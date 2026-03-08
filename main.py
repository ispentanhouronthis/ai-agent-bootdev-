import os
from prompts import system_prompt
import argparse
import sys
from google import genai    
from dotenv import load_dotenv
from call_function import available_functions,call_function
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    user_prompts= args.user_prompt
    is_verbose=args.verbose


    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    if api_key==None:
        raise RuntimeError("Invalid api key")

    client = genai.Client(api_key=api_key)
    
    for _ in range(20):
        gen_content = client.models.generate_content(model='gemini-2.5-flash',contents= messages, config=genai.types.GenerateContentConfig(system_instruction=system_prompt,temperature=0,tools=[available_functions]))
        if gen_content.candidates!=None:
            for candidates in gen_content.candidates:
                messages.append(candidates.content)
        if gen_content.usage_metadata==None:
            raise RuntimeError("Failed api Response")
        elif is_verbose==True:
            print(f"User prompt: {user_prompts}")

            print(f"Prompt tokens: {gen_content.usage_metadata.prompt_token_count}")

            print(f"Response tokens: {gen_content.usage_metadata.candidates_token_count}")

        function_results=[]
        
        if gen_content.function_calls != None:
            for function_call in gen_content.function_calls:
                function_call_result= call_function(function_call,is_verbose)
                if len(function_call_result.parts)==0:
                    raise Exception(".parts list is empty")
                if function_call_result.parts[0].function_response==None:
                    raise Exception("FunctionResponse object not found")
                if function_call_result.parts[0].function_response.response==None:
                    raise Exception("Response not generated")
            
                if is_verbose==True:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                function_results.append(function_call_result.parts[0])
    
            messages.append(types.Content(role="user", parts=function_results))

        else:
            print(f"Response: \n{gen_content.text}")
            break
    else:
        print("max iterations(20) reached but no response")
        sys.exit(1)
           
    
   


if __name__ == "__main__":
    main()
