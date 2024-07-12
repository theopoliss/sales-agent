from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")


    def sales_manager(self):
        return Agent(
            role="Sales Manager",
            backstory=dedent(f"""As the Sales Manager, your mission is to oversee the sales team and ensure
                             that they are meeting their targets. You will be responsible for setting sales
                             targets, monitoring the team's performance, and providing guidance and support
                             to help them succeed. You will also be responsible for developing sales strategies
                             and identifying new opportunities for growth."""),
            goal=dedent(f"""Increase the sales team's performance and meet or exceed sales targets."""),
            # tools=[tool_1, tool_2],
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def lead_generator(self):
        return Agent(
            role="Lead Generator",
            backstory=dedent(f"""Expert in finding leads and prospects with decades of experience identifying leads.
                             Within the sales team, your mission is to scour the digital landscape to
                             identify potential leads and prospects. By finding leads and potential prospects,
                             you will help the sales team build the sales pipeline."""),
            goal=dedent(f"""Identify high-value leads that match our ideal customer profile."""),
            tools=[self.search_tool, self.scrape_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def prospect_researcher(self):
        return Agent(
            role="Prospect Researcher",
            backstory=dedent(f"""As part of the dynamic sales team, your mission is to research the leads 
                             that were generated. By using online tools like LinkedIn, you will help the sales team
                             identify key decision-makers and influencers within the target companies.
                             Normally, these decision-makers will be facility or office managers.
                             Your role is to provide the sales team with important information that will assist
                             them when speaking with the prospects in the field."""),
            goal=dedent(f"""Find key decision makers (facility or office managers) within the potential prospects
                        and find their emails"""),
            tools=[self.search_tool, self.scrape_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )