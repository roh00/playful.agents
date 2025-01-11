# from transformers import AutoModelForCausalLM, AutoTokenizer
#
# # Load the model and tokenizer
# model_name = "gpt2"  # You can replace this with "EleutherAI/gpt-neo-1.3B" or others
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)
#
# # Define a prompt
# prompt = " how can i earn money and get rich via AI"
#
# # Tokenize and generate a response
# inputs = tokenizer(prompt, return_tensors="pt")
# outputs = model.generate(inputs.input_ids, max_length=100, num_return_sequences=1, temperature=0.7)
#
# # Decode and print the response
# response = tokenizer.decode(outputs[0], skip_special_tokens=True)


# Deploy this script on some webserver via docker for free



# print(response)
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

# from transformers.models.pop2piano.convert_pop2piano_weights_to_hf import model
load_dotenv()
web_agent = Agent(
    name='astro_web',
    role="Know about a person",
    model=Groq(id="llama-3.2-11b-vision-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always use sources"],
    show_tool_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name='astro_financial',
    role="Know about a person financially",
    model=Groq(id="llama-3.2-11b-vision-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Always use sources"],
    show_tool_calls=True,
    markdown=True,
)

# multi_agent = Agent(
#     model=Groq(id="llama-3.2-11b-vision-preview"),
#     team=[web_agent, financial_agent],
#     instructions=["Always use sources", "Use table to show data"],
#     show_tool_calls=True,
#     markdown=True,
# )

# web_agent.print_response("My date of birth is 18/06/1998 and time is 5:45 pm, what is my sun sign and also give me some prediction about me, could you generate response in hindi")