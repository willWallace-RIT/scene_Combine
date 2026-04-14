# Scene Combiner

Merges reconstructed static scene layers into a unified path dataset.

## Features
- Multi-layer path merging
- Coordinate transform normalization
- Timestamp alignment
- Duplicate suppression
- Noise smoothing support

## Use Case
- Game replay reconstruction
- Camera/player trajectory analysis
- Geo-based inference systems
- Scene understanding pipelines

## Example

```python
combiner = SceneCombiner()
combiner.add_layer(layer_a)
combiner.add_layer(layer_b)

result = combiner.combine()
