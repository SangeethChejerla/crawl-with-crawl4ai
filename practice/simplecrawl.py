import asyncio

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig


async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://vercel.com/enterprise",
        )
        print(result.markdown)


if __name__ == "__main__":
    asyncio.run(main())
