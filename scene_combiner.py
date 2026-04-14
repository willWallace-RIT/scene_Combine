import numpy as np
from path_models import SceneLayer, Path, PathPoint


class SceneCombiner:

    def __init__(self):
        self.layers = []

    def add_layer(self, layer: SceneLayer):
        self.layers.append(layer)

    def _apply_transform(self, point: PathPoint, matrix):
        if matrix is None:
            return point

        vec = np.array([point.x, point.y, point.z, 1.0])
        tx, ty, tz, _ = matrix @ vec

        return PathPoint(tx, ty, tz, point.t)

    def _normalize_layer(self, layer: SceneLayer):
        transformed_paths = []

        for path in layer.paths:
            new_points = [
                self._apply_transform(p, layer.transform_matrix)
                for p in path.points
            ]
            transformed_paths.append(
                Path(
                    id=path.id,
                    type=path.type,
                    points=new_points
                )
            )

        return transformed_paths

    def combine(self):
        merged = {}

        for layer in self.layers:
            paths = self._normalize_layer(layer)

            for path in paths:
                key = f"{path.type}:{path.id}"

                if key not in merged:
                    merged[key] = path.points
                else:
                    merged[key].extend(path.points)

        # post-process cleanup
        return self._deduplicate_and_sort(merged)

    def _deduplicate_and_sort(self, merged):
        output = {}

        for key, points in merged.items():
            # sort by time
            points = sorted(points, key=lambda p: p.t)

            # remove near-duplicates
            cleaned = []
            last = None

            for p in points:
                if last is None:
                    cleaned.append(p)
                    last = p
                    continue

                dist = ((p.x - last.x)**2 + (p.y - last.y)**2 + (p.z - last.z)**2) ** 0.5

                if dist > 0.01 or abs(p.t - last.t) > 0.05:
                    cleaned.append(p)
                    last = p

            output[key] = cleaned

        return output
