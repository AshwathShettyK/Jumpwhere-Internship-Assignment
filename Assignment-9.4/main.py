# Convert Negative Coordinates to Positive Coordinates
# Translates a list of 2D points so all x and y values are non-negative.


def calculate_shift(points):
    """Return x and y shift values needed to make all coordinates non-negative."""
    if not points:
        return 0, 0

    min_x = min(x for x, _ in points)
    min_y = min(y for _, y in points)

    x_shift = -min_x if min_x < 0 else 0
    y_shift = -min_y if min_y < 0 else 0
    return x_shift, y_shift


def translate_points(points, x_shift, y_shift):
    """Translate points by the given x and y shift values."""
    translated = []
    for x, y in points:
        translated.append((x + x_shift, y + y_shift))
    return translated


def display_points(points):
    """Print the list of coordinates in a readable format."""
    print(points)


def main():
    original_points = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]

    print("Original Coordinates\n")
    display_points(original_points)

    x_shift, y_shift = calculate_shift(original_points)
    print(f"\nX Shift : {x_shift}")
    print(f"Y Shift : {y_shift}\n")

    translated_points = translate_points(original_points, x_shift, y_shift)

    print("Converted Coordinates\n")
    display_points(translated_points)


if __name__ == "__main__":
    main()
