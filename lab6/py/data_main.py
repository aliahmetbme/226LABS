from data_package import remove_duplicates, strip_whitespaces, calculate_mean, find_maximum, find_minimum

def main():
    user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")
    
    # Split the input into a list of strings
    string_list = user_input.split(',')
    
    # Clean the input: strip whitespaces
    stripped_list = strip_whitespaces(string_list)
    
    # Remove empty strings in case of trailing/multiple commas
    stripped_list = [s for s in stripped_list if s]

    try:
        # Convert strings to floats
        num_list = [float(s) for s in stripped_list]
    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")
        return

    # Use cleaner to remove duplicates
    unique_numbers = remove_duplicates(num_list)

    if not unique_numbers:
        print("Data Error: No valid numbers provided.")
        return

    # Analyze data
    mean_val = calculate_mean(unique_numbers)
    max_val = find_maximum(unique_numbers)
    min_val = find_minimum(unique_numbers)

    print(f"Cleaned and unique data: {unique_numbers}")
    print("-" * 20)
    print(f"Mean: {mean_val:.2f}")
    print(f"Maximum: {max_val}")
    print(f"Minimum: {min_val}")

if __name__ == "__main__":
    main()
