import geometry_utils

def main():
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")
    operation = input("Enter the operation you want to perform: ").strip().lower()

    operations = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    if operation not in operations:
        print("Invalid operation entered.")
        return

    try:
        if operation.startswith("circle"):
            radius = float(input("Enter radius: "))
            result = operations[operation](radius)
        elif operation.startswith("rectangle"):
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = operations[operation](width, height)
        elif operation.startswith("triangle"):
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = operations[operation](base, height)
        
        print(f"Result: {result:.2f}")

    except ValueError as e:
        if "could not convert" in str(e).lower() or "invalid literal" in str(e).lower():
            print("Input Error: Please enter numerical values.")
        else:
            msg = str(e)
            if not msg.endswith('.'):
                msg += '.'
            print(f"Input Error: {msg}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
