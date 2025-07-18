# arxiv_tool.py
import arxiv

def fetch_arxiv_papers(query, max_results=5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "url": result.entry_id,
            "authors": [author.name for author in result.authors],
            "published": result.published.strftime("%Y-%m-%d")
        })
    return papers

