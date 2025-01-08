from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

from dotenv import load_dotenv

load_dotenv()

web_search_agent = Agent(
    name="Web Agent",
    description="Agente para pesquisar conteudo da web",
    model=Groq(id="llama3-70b-8192"), # llama3-groq-70b-8192-tool-use-preview
    tools=[DuckDuckGo()],
    instructions="Sempre inclua as fontes",
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

# web_search_agent.print_response("Qual a capital do Brasil?", stream=True)
# web_search_agent.print_response("Traga me uma lista de todas os municipios do Brasil traga em formato JSON", stream=True)

financas_agente = Agent(
    name="Agente Financeiro",
    description="Tarefa encontrar as informações financeiras",
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tabelas para mostrar os dados"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

# financas_agente.print_response("Resumir informações de analistas do mercado para NVDA", stream=True)

time_agente = Agent(
    team=[web_search_agent, financas_agente],
    model=Groq(id="llama3-70b-8192"),
    instructions=["Sempre inclua as fontes, URL e links", "Use tabelas para mostrar os dados"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
    
)

time_agente.print_response("Resumir informações de analistas do mercado e as ultimas noticias para NVDA", stream=True)
