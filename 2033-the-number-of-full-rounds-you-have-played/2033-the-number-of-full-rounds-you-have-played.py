class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        start_hour, start_minutes = int(loginTime[:2]), int(loginTime[3:])
        end_hour, end_minutes = int(logoutTime[:2]), int(logoutTime[3:])            
        if start_minutes > 45:
            start_minutes = 0
            start_hour += 1
        elif start_minutes > 30:
            start_minutes = 45
        elif start_minutes > 15:
            start_minutes = 30
        elif start_minutes > 0:
            start_minutes = 15       
        
        if end_minutes < 15:
            end_minutes = 0
        elif end_minutes < 30:
            end_minutes = 15
        elif end_minutes < 45:
            end_minutes = 30
        elif end_minutes <= 59:
            end_minutes = 45
        
        if logoutTime < loginTime:
            end_hour += 24
        
        total_minutes = (end_hour - start_hour) * 60 - start_minutes + end_minutes

        # total_minutes = 0
        # if end_hour == start_hour:
        #     total_minutes = end_minutes - start_minutes
        # elif end_hour >= start_hour:
        #     total_minutes = (end_hour - start_hour) * 60 - start_minutes + end_minutes
        # else:
        #     # end_hour += 24
        #     total_minutes = (end_hour - start_hour) * 60 - start_minutes + end_minutes
      
        return total_minutes // 15 if total_minutes > 0 else 0