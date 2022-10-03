from fluent.vector2d import Vector


def test_add_two_vectors():
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    assert abs(v1 + v2) == abs(Vector(4, 5))


def test_vector_has_magnitude():
    v = Vector(3, 4)
    assert abs(v) == 5


def test_can_multiply_vector_by_scalar():
    v = Vector(3, 4)
    v3 = v * 3
    assert abs(v3) == 15
