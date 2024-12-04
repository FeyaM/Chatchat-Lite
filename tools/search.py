from langchain_core.tools import tool

@tool
def weather_search(query: str):
    """Call to surf the web."""
    # This is a placeholder, but don't tell the LLM that...
    print(query)
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."