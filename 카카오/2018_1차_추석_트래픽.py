def solution(lines):
    times = []

    # 로그를 (start, end)로 변환
    for line in lines:
        date, time, duration = line.split()
        h, m, s = time.split(':')
        end = (int(h) * 3600 + int(m) * 60 + float(s)) * 1000
        duration = float(duration[:-1]) * 1000
        start = end - duration + 1
        times.append((start, end))

    answer = 0
    # 모든 로그의 start, end 기준으로 1초 구간 체크
    for s, e in times:
        for t in [s, e]:
            start_window = t
            end_window = t + 999
            cnt = 0
            for s2, e2 in times:
                if e2 >= start_window and s2 <= end_window:  # 구간 겹치면
                    cnt += 1
            answer = max(answer, cnt)

    return answer
