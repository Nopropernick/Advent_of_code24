def is_safe_report(report):
    """
    Check if a single report is safe based on the given conditions.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are within the range [1, 3] or [-3, -1]
    if all(1 <= diff <= 3 for diff in differences):  # Increasing
        return True
    elif all(-3 <= diff <= -1 for diff in differences):  # Decreasing
        return True
    else:
        return False

def count_safe_reports(file_path):
    """
    Read the input file, process the reports, and count the number of safe reports.
    """
    safe_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                report = list(map(int, line.split()))
                if is_safe_report(report):
                    safe_count += 1
    
    return safe_count

# Example usage
file_path = r"D:\Advent of Code\day2.txt"  # Replace with the actual file path
safe_reports_count = count_safe_reports(file_path)
print(f"Number of Safe Reports: {safe_reports_count}")
