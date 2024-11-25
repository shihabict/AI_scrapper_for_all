import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph
import json

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_key = os.getenv("OPENAI_APIKEY")

# Configuration for the SmartScraperGraph
graph_config = {
   "llm": {
      "api_key": openai_key,
      "model": "gpt-3.5-turbo",
   },
}

# Create the SmartScraperGraph instance and run it
smart_scraper_graph = SmartScraperGraph(
   # prompt="List me all the product and their price.",
   prompt="List me all the branches and office name and country with their address and phone numbers, contact emails if available.",
   # prompt="You are an expert content summarizer.You take organization about page content and prepare a short summary about the company. Combine all of your understanding of the content, and Prepare a brief summary about the company and do not hallucinate too much",
   # source can also accept a string with the already downloaded HTML code
   source="https://brainstation-23.com/contact/",
   # source="https://www.kikcorp.com/contact-us/",
   # source="https://reasonclothing.com/collections/lil-wayne",
   config=graph_config
)

# Execute the scraper and save the results to a JSON file
result = smart_scraper_graph.run()
with open("results.json", 'w', encoding='utf-8') as f:
      json.dump(result, f, indent=4)