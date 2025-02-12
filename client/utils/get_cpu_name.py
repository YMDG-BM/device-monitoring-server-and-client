import pygetwindow as gw

def get_active_window():
    try:
        window = gw.getActiveWindow()
        if window is not None:
            return {
                'title': window.title,
                'hwnd': window._hWnd
            }
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


while True:
    active_window = get_active_window()
    if active_window:
        print(f"Active Window: {active_window['title']} (HWND: {active_window['hwnd']})")
    else:
        print("No active window found or unable to retrieve the active window.")
