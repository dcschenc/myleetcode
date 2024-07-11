from multiprocessing.pool import ThreadPool
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def helper(url):
            to_process.remove(url)
            for new_url in htmlParser.getUrls(url):
                if new_url[:len(host)] == host and new_url not in res:
                    res.add(new_url)
                    to_process.add(new_url)

        to_process = set()
        res = set()
        res.add(startUrl)
        to_process.add(startUrl)
        host = 'http://' + startUrl.split('/')[2]           
        p = ThreadPool(18)
        while to_process:
            p.map(helper, list(to_process))
        return res