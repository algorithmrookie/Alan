class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sn = len(s)
        tn = len(t)
        
        res_start = -1
        res_len = float('inf')

        need_cnt = tn
        need_char_cnt = defaultdict(int)
        for c in t:
            need_char_cnt[c] += 1

        l = 0
        for r in range(sn):
            if s[r] in need_char_cnt:
                if need_char_cnt[s[r]] > 0:
                    need_cnt -= 1
                need_char_cnt[s[r]] -= 1
            if need_cnt == 0:
                while True: 
                    if s[l] not in need_char_cnt:
                        l += 1
                    else:
                        if need_char_cnt[s[l]] < 0:
                            need_char_cnt[s[l]] += 1
                            l += 1
                        else:
                            break
                cur_len = r - l + 1
                if cur_len < res_len:
                    res_len = cur_len
                    res_start = l
        if res_start != -1:
            return s[res_start: res_start + res_len]
        return ""
