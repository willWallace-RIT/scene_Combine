def smooth_path(points, window=5):
    smoothed = []

    for i in range(len(points)):
        chunk = points[max(0, i-window):i+1]

        x = sum(p.x for p in chunk) / len(chunk)
        y = sum(p.y for p in chunk) / len(chunk)
        z = sum(p.z for p in chunk) / len(chunk)

        smoothed.append(type(points[i])(x, y, z, points[i].t))

    return smoothed
