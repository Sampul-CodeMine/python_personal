class DiGraph:
    def __init__(self, edges):
        self.adj = {}
        for u, v in edges:
            if u not in self.adj:
                self.adj[u] = [v]
            self.adj[u].append(v)

    def __str__(self):
        return '\n'.join(['%s -> %s' % (u, v) for u in self.adj for v in self.adj[u]])
        # The above comment is the short form of the code below.
        # val = ""
        # for u in self.adj:
        #     for v in self.adj[u]:
        #         val += '\n'.join(['%s -> %s\n' % (u, v)])
        # return val


def reverse(data):
    for i in range(len(data)):
        yield data[len(data) -1-i]


for char in reverse('spam'):
    print(char)

print("================================")

d = DiGraph([(1, 2), (1, 3), (2, 4), (4, 3), (4, 1)])
print(d)