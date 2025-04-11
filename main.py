from openai import OpenAI
from dotenv import dotenv_values
from tools.tools import get_current_weather, get_location
import re

config = dotenv_values('.env')

openai = OpenAI(
    api_key = config['OPENAI_API_KEY']
)

available_functions = {
    "get_current_weather":get_current_weather,
    "get_location":get_location
}

system_prompt = '''

You cycle through Thought, Action, PAUSE, Observation. At the end of the loop you output a final Answer. Your final answer should be highly specific to the observations you have from running
the actions.
1. Thought: Describe your thoughts about the question you have been asked.
2. Action: run one of the actions available to you - then return PAUSE.
3. PAUSE
4. Observation: will be the result of running those actions.

Available actions:
- get_current_weather: 
    E.g. get_current_weather: Salt Lake City
    Returns the current weather of the location specified.
- get_location:
    E.g. get_location: null
    Returns user's location details. No arguments needed.

Example session:
Question: Please give me some ideas for activities to do this afternoon.
Thought: I should look up the user's location so I can give location-specific activity ideas.
Action: get_location: null
PAUSE

You will be called again with something like this:
Observation: "New York City, NY"

Then you loop again:
Thought: To get even more specific activity ideas, I should get the current weather at the user's location.
Action: get_current_weather: New York City
PAUSE

You'll then be called again with something like this:
Observation: { "location": "New York City, NY", "forecast": ["sunny"] }

You then output:
Answer: <Suggested activities based on sunny weather that are highly specific to New York City and surrounding areas.>

'''

def agent(query):
    chat_messages = [
        {"role":"system", "content":system_prompt},
        {"role":"user", "content":query}
    ]
    
    MAX_ITERATIONS = 5
    action_regex = r"Action: (\w+): (.*)"
    
    for x in range (MAX_ITERATIONS):
        print(f"DEBUG::Iteration {x + 1}")
        
        response = openai.chat.completions.create(
            model='gpt-4',
            messages=chat_messages
        )
        
        response_text = response.choices[0].message.content
        print('DEBUG::', response_text)
        
        chat_messages.append({"role":"assistant", "content":response_text})
        response_lines = response_text.split('\n')
        
        action_str = ""
        
        for str in response_lines:
            if "Action:" in str:
                action_str = str
        
        if(action_str):
            match = re.search(action_regex, action_str)
            action = match.group(1)
            action_arg = match.group(2)
            
            if action_arg == 'null':
                action_arg = None
            
            if action not in available_functions:
                print("ERROR::Unknown funtion.", action)
                break
            
            print(f"DEBUG::Calling function {action} with argument {action_arg}")
            
            if action_arg:
                observation = available_functions[action](action_arg)
            else:
                observation = available_functions[action]()
            
            chat_messages.append({ "role": "assistant", "content": f"Observation: {observation}" })
        else:
            print("DEBUG::Agent finished with task")
            return response_text
            
        
if __name__ == "__main__":
    query = "What are some activity ideas that I can do this afternoon based on my location and weather?"
    answer = agent(query)
    print("#######################################################")
    print(answer)
    print("#######################################################")
    