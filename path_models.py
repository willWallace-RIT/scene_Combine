from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass
class PathPoint:
    x: float
    y: float
    z: float = 0.0
    t: float = 0.0  # timestamp


@dataclass
class Path:
    id: str
    points: List[PathPoint]
    type: str  # "player", "camera", "object"


@dataclass
class SceneLayer:
    id: str
    paths: List[Path]
    transform_matrix: Optional[list] = None  # 4x4 optional
