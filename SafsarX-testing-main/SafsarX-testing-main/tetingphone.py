import re
import subprocess
from datetime import datetime

def get_latest_sms():
    try:
        # Run ADB command to fetch SMS messages
        result = subprocess.run(
            ["adb", "shell", "content", "query", "--uri", "content://sms/inbox", "--projection", "body:date"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8'  # Explicitly specify encoding
        )

        # Check if there's an error in the output
        if result.returncode != 0:
            # Print the error for debugging
            print(f"Error fetching SMS: {result.stderr}")
            return None

        # Check if the stdout is not empty before attempting to split it
        if result.stdout:
            messages = result.stdout.splitlines()

            # Extract and parse each message
            parsed_messages = []
            for message in messages:
                # Assuming messages are formatted as "Row <n> body=<text>, date=<timestamp>"
                parts = message.split(", ")

                # Ensure the message has both body and date fields
                if len(parts) >= 2:
                    try:
                        body_part = parts[0].split("=", 1)[1].strip()
                        date_part = parts[1].split("=", 1)[1].strip()

                        # Check if the date is numeric and represents a reasonable timestamp
                        if date_part.isdigit():
                            timestamp = int(date_part)
                            # Ensure the timestamp is in a reasonable range (not too far in the future/past)
                            # We consider anything in the range of 1970-01-01 to some years in the future reasonable
                            if 0 <= timestamp <= 2000000000000:  # Roughly up to year 2033
                                parsed_messages.append((body_part, timestamp))

                    except IndexError:
                        # Skip this line if it doesn't conform to the expected format
                        continue

            # Sort messages by date and get the latest one
            if parsed_messages:
                # Convert date strings to datetime objects for sorting
                parsed_messages.sort(key=lambda x: x[1], reverse=True)  # Sort by timestamp in descending order
                latest_sms = parsed_messages[0]  # Get the latest message
                return latest_sms[0]  # Return the body of the latest SMS

            print("No valid messages found.")
            return None

    except subprocess.SubprocessError as e:
        print(f"An error occurred while running adb command: {e}")
        return None


# Example usage
if __name__ == "__main__":

	latest_sms = get_latest_sms()
	# מתקבל סטרינג שמכיל את הקוד אבל תריך עדיין לחלצו
	if latest_sms:
		print(f"Latest SMS: {latest_sms}")
	else:
		print("Failed to fetch the latest SMS.")



output = latest_sms
ver_code = [int(word) for word in output.split() if word.isdigit()]
print(ver_code)

