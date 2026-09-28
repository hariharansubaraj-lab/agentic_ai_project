import asyncio

from app.async_runner import run_tools_concurrently


async def main():

    print("=" * 60)
    print("     PRACTICE 5 - ASYNC TOOL EXECUTION")
    print("=" * 60)

    calculator_result, search_result = (
        await run_tools_concurrently()
    )

    print("\n" + "=" * 60)
    print("CALCULATOR RESULT")
    print("=" * 60)

    print(calculator_result)

    print("\n" + "=" * 60)
    print("WEB SEARCH RESULT")
    print("=" * 60)

    print(search_result)


if __name__ == "__main__":
    asyncio.run(main())