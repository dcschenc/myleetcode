class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        days = -inf
        for job, worker in zip(jobs, workers):
            days = max(math.ceil(job/worker), days)
        return days