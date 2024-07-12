from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from utils import get_openai_api_key,get_serper_api_key
import os

os.environ["SERPER_API_KEY"] = get_serper_api_key()
os.environ["OPENAI_API_KEY"] = get_openai_api_key()

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()