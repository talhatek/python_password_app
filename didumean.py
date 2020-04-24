from numpy import sum
import numpy as np

def frombeg(a, node_keys, x):
    scores = []
    for item in node_keys:
        beg = 0
        cnt = 0
        if len(x) > len(item):
            for i in range(len(item)):

                if a[i] == item[i]:
                    cnt = cnt + 1
                    beg = beg + 1
                    if cnt == len(item):
                        scores.append(cnt)
                        break
                else:
                    scores.append(beg)
                    break
        else:
            for i in range(len(x)):
                if a[i] == item[i]:
                    beg = beg + 1
                    cnt = cnt + 1
                    if cnt == len(x):
                        scores.append(cnt)
                        break
                else:
                    scores.append(beg)
                    break

    return scores


def fromend(a, node_keys, x):
    scores = []
    a.reverse()
    for item in node_keys:
        rvs = item[::-1]
        beg = 0
        cnt = 0
        if len(x) > len(item):
            for i in range(len(item)):
                if (a[i] == rvs[i]):
                    cnt = cnt + 1
                    beg = beg + 1
                    if (cnt == len(item)):
                        scores.append(cnt)
                        break
                else:
                    scores.append(beg)
                    break
        else:
            for i in range(len(x)):
                if (a[i] == rvs[i]):
                    beg = beg + 1
                    cnt = cnt + 1
                    if (cnt == len(x)):
                        scores.append(cnt)
                        break
                else:
                    scores.append(beg)
                    break

    return scores


def decide(result1, result2, node_keys):
    merged = sum([result1, result2], axis=0)
    toList = list(merged)
    maxvalue = max(toList)
    maxindex = toList.index(maxvalue)
    print(np.count_nonzero(merged))
    return (node_keys[maxindex]) if np.count_nonzero(merged) > 0 else None




def u_mean(unsplitted, node_keys):
    splitted_by_chars = list(unsplitted.lower())
    fb = frombeg(splitted_by_chars, [x.lower() for x in node_keys], unsplitted)
    fe = fromend(splitted_by_chars, [x.lower() for x in node_keys], unsplitted)
    sonuc = decide(fb, fe, node_keys)
    return sonuc

