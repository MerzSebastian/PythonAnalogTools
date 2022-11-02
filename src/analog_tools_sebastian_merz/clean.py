
def clean(data, threshold = None):
    threshold = statistics.median([min(data[1]), max(data[1])]) if threshold == None else threshold
    clean_data = [[],[]]
    for i in range(0, len(data[0])-1):
        status = lambda i: data[1][i] >= threshold
        #status = data[1][i] >= threshold
        #status_next = data[1][i+1] >= threshold
        if status != status_next or i == 0:
            clean_data[0].append(data[0][i])
            clean_data[1].append(int(status(i)))
            clean_data[0].append(data[0][i+1])
            clean_data[1].append(int(status(i+1)))
    clean_data[0].append(max(data[0]))
    clean_data[1].append(int(data[1][len(data[1])-1] >= threshold))
    return clean_data