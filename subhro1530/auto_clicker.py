import pyautogui
import time

# Function to wait for a specific image to appear on the screen
def wait_for_image(image_path, timeout=10):
    start_time = time.time()

    while time.time() - start_time < timeout:
        # Check if the image is present on the screen
        if pyautogui.locateOnScreen(image_path):
            return True
        time.sleep(1)

    return False

# Function to click a button and handle popups
def click_button_with_popup_handling(button_image, popup_image, num_clicks):
    try:
        for _ in range(num_clicks):
            # Wait for the popup and handle it
            if wait_for_image(popup_image):
                print("Popup detected. Handling...")
                # Add your code to handle the popup (e.g., close it)
                # For demonstration purposes, let's print a message
                print("Popup handled.")

            # Find the button's location on the screen
            button_location = pyautogui.locateOnScreen(button_image)

            if button_location is None:
                print("Button not found on the screen.")
                return

            # Get the center coordinates of the button
            button_center = pyautogui.center(button_location)

            # Click the button
            pyautogui.click(button_center)

            # Add a small delay between clicks (adjust as needed)
            time.sleep(0.5)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage with the path set to '/click.png'
button_image_path = 'click.png'
popup_image_path = 'popup.png'
num_clicks = 5

# Call the function to click the button with popup handling
click_button_with_popup_handling(button_image_path, popup_image_path, num_clicks)
