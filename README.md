# AI Agent Demo

A simple AI agent demonstration built as part of the Scrimba AI Engineering Path. This project showcases how to create a basic reactive agent using OpenAI's API with a tool-using pattern.

## Overview

This AI agent can:
- Access the user's location (hard coded for the demo)
- Get current weather information (hard coded for the demo)
- Suggest activities based on location and weather conditions
- Follow a "Reasoning, Action, Observation" cycle, "ReAct"

The agent demonstrates the fundamental pattern of an AI that can reason about its environment, take actions, and incorporate the results of those actions into its ongoing reasoning process.

## Features

- **Tool Usage**: Showcases how to create and implement function-calling with OpenAI
- **Reasoning Cycles**: Implements a structured reasoning pattern
- **Location Awareness**: Can determine user location
- **Weather Integration**: Can fetch current weather data
- **Contextual Recommendations**: Provides activity suggestions based on gathered data

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for API calls

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/dulakshanwije/simple-ai-agent-demo.git
   cd simple-ai-agent-demo
   ```

2. Install dependencies:
   ```
   pip install openai python-dotenv
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the main script to start the agent:

```
python main.py
```

By default, the agent will respond to the query: "What are some activity ideas that I can do this afternoon based on my location and weather?"

To customize the query, modify the `query` variable in the `if __name__ == "__main__":` block at the bottom of the script.

## Project Structure

- `main.py`: Main script containing the agent implementation
- `tools/tools.py`: Contains the tool functions (`get_current_weather` and `get_location`)
- `.env`: Environment variables file for API keys (not included in repo)

## How It Works

1. The agent receives a query from the user
2. It follows a structured reasoning pattern:
   - **Thought**: Reasoning about what information it needs
   - **Action**: Calling an external function like getting location or weather
   - **PAUSE**: Waiting for the function result
   - **Observation**: Processing the result of the action
3. This cycle repeats up to 5 times or until the agent has enough information
4. Finally, the agent provides a comprehensive answer based on the observations

## Acknowledgments

- This project was created as part of the Scrimba AI Engineering Path
