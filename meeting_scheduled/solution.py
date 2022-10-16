import heapq

# O(nlogn)

m, k = [int(i) for i in input().split(' ')]
q = []
for i in range(m):
    t1_h, t1_m, t2_h, t2_m = input().split(' ')
    # convert to minutes and add to min heap with start time as key
    t1 = int(t1_h) * 60 + int(t1_m)
    t2 = int(t2_h) * 60 + int(t2_m)
    # edge case t2 = 00:00 when t2 < t1
    if t2 < t1 and t2 == 0:
        t2 = 24 * 60
    heapq.heappush(q, (t1, t2))


prev_end = 0
# loop through m inputs
while q:
    t1, t2 = heapq.heappop(q)
    # diff previous end time and current start time
    x = t1 - prev_end
    if x >= k:
        # if K duration slot is found convert start and end time from minutes to output format and print
        h1 = int(prev_end / 60)
        m1 = int(prev_end % 60)
        h2 = int(t1 / 60)
        m2 = int(t1 % 60)
        print(str(h1).zfill(2) + ' ' + str(m1).zfill(2) + ' ' + str(h2).zfill(2) + ' ' + str(m2).zfill(2))
    # if current end time is less than previously seen end time, use previously seen end time for next loop
    prev_end = max(prev_end, t2)


# remaining time check
end = 24 * 60
if end - prev_end >= k:
    h1 = int(prev_end / 60)
    m1 = int(prev_end % 60)
    h2 = 0
    m2 = 0
    print(str(h1).zfill(2) + ' ' + str(m1).zfill(2) + ' ' + str(h2).zfill(2) + ' ' + str(m2).zfill(2))