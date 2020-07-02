from typing import Any

from turf.boolean_disjoint import boolean_disjoint


def boolean_intersects(feature_1: Any, feature_2: Any) -> bool:

    return not boolean_disjoint(feature_1, feature_2)
