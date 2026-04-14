import numpy as np

def align_layers(reference_points, target_points):
    """
    Simple centroid alignment (can upgrade to ICP later)
    """

    ref = np.mean([[p.x, p.y, p.z] for p in reference_points], axis=0)
    tgt = np.mean([[p.x, p.y, p.z] for p in target_points], axis=0)

    offset = ref - tgt

    aligned = []
    for p in target_points:
        aligned.append(type(p)(
            x=p.x + offset[0],
            y=p.y + offset[1],
            z=p.z + offset[2],
            t=p.t
        ))

    return aligned
