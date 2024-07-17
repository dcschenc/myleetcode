class Solution:
    def reformatDate(self, date: str) -> str:
        s = date.split()
        s.reverse()
        months = " JanFebMarAprMayJunJulAugSepOctNovDec"
        s[1] = str(months.index(s[1]) // 3 + 1).zfill(2)
        s[2] = s[2][:-2].zfill(2)
        return "-".join(s)
        
        month_hm = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        arr = date.split()
        arr.reverse()
        res = arr[0] + "-" + month_hm[arr[1]] + "-"
        day = ''
        for c in arr[2]:
            if c in '0123456789':
                day += c
        if len(day) == 1:
            day = '0' + day
        res = res + day
        return res
