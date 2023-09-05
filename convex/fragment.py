max_dist = self._diameter
j = self.points.size() - 1
while 0 < j:
    dist_j = t.dist(self.points.array[j])
        if dist_j > max_dist:
            max_dist = dist_j
        else:
            j -= 1
self._diameter = max_dist