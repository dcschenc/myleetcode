# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url):
            hostname = url[7:]
            idx = hostname.find('/')
            if idx != -1:
                hostname = hostname[:idx]
            return hostname

        def dfs(startUrl):
            if startUrl in visited:
                return
            visited.add(startUrl)
            if get_hostname(startUrl) == hostname:
                if startUrl not in ans: 
                    ans.add(startUrl)
                for url in htmlParser.getUrls(startUrl):
                    dfs(url)

        ans, visited = set(), set()
        hostname = get_hostname(startUrl)
        # print(hostname)
        dfs(startUrl)
        return ans