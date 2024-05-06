import re
import sys

def parse_log_line(line: str) -> dict:
    """Parse a log line and return a dictionary with date, time, level, and message."""
    pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.*)'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return {}

def load_logs(file_path: str) -> list:
    """Load logs from the file and return a list of parsed log dictionaries."""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log = parse_log_line(line.strip())
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print("Error: Log file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by the specified log level."""
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    """Count the number of logs for each log level."""
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict):
    """Display log counts in a formatted table."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    total = sum(counts.values())
    for level, count in counts.items():
        print(f"{level:<17} | {count}")
    print("\nTotal logs:", total)

def display_logs(logs: list):
    """Display detailed logs."""
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [log_level]")
        sys.exit(1)
    
    log_file = sys.argv[1]
    log_level = None
    if len(sys.argv) > 2:
        log_level = sys.argv[2]

    logs = load_logs(log_file)
    if logs:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        
        if log_level:
            filtered_logs = filter_logs_by_level(logs, log_level)
            print("\nDetails for log level:", log_level)
            display_logs(filtered_logs)
    else:
        print("No logs found.")