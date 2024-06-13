def mergeIntervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()
    
    mergedIntervals = []
    currentStart, currentEnd = intervals[0]
    
    for start, end in intervals[1:]:
        if currentEnd >= start: 
            currentEnd = max(currentEnd, end)
        else:
            mergedIntervals += [(currentStart, currentEnd)]
            currentStart, currentEnd = start, end
    
    mergedIntervals += [(currentStart, currentEnd)]
    
    return mergedIntervals

intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
merged = mergeIntervals(intervals)
print("Merged Intervals:", merged)
