import asyncio

from app.tools import calculator, web_search


async def run_tools_concurrently():
    print("\nStarting 2 tools concurrently...\n")

    # Tool 1
    calculator_task = calculator.ainvoke("25 * 4")

    # Tool 2
    search_task = web_search.ainvoke(
        "Latest developments in Artificial Intelligence"
    )

    # Run both tools at the same time
    calculator_result, search_result = await asyncio.gather(
        calculator_task,
        search_task
    )

    return calculator_result, search_result