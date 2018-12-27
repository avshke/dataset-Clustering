import json
import matplotlib.pyplot as plt


def parse_json():
    clusters = []
    with open('ex1.json', encoding='utf-8') as f:
        data = json.load(f)["records"]["record"]
    for i in range(len(data)):
        if data[i]["Currency"] == '$' and data[i]["DolarsPelged"] is not None:
            clusters.append([data[i]["DolarsPelged"]])
    return clusters


def find_center(cluster):
    sum = 0
    for num in cluster:
        sum += num
    return sum / len(cluster)


def find_diameter(cluster):
    return max(cluster) - min(cluster)


def merge_clusters(clusters, type_cluster):
    min_dis = 1332642
    clus1 = []
    clus2 = []
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            if type_cluster == "centroid":
                distance = abs(find_center(clusters[i]) - find_center(clusters[j]))
            elif type_cluster == "diameter":
                distance = find_diameter(clusters[i] + clusters[j])
            if distance < min_dis:
                clus1, clus2 = clusters[i], clusters[j]
                min_dis = distance
    clus1 += clus2
    clusters.remove(clus2)
    return min_dis


def cluster_a():
    clusters = parse_json()
    steps = 0
    distances = []
    while len(clusters) > 1:
        distances.append(merge_clusters(clusters, "centroid"))
        steps += 1

    plt.plot(range(steps), distances)
    plt.show()


def cluster_b():
    clusters = parse_json()
    steps = 0
    distances = []
    while len(clusters) > 1:
        distances.append(merge_clusters(clusters, "diameter"))
        steps += 1

    plt.plot(range(steps), distances)
    plt.show()

