try:
    x = int(input("Please enter a number: "))
    y = 100 / x
except ValueError:
    print("Error: there was an error")
except ZeroDivisionError:
    print("Error: 0 is an invalid number")
except Exception:
    print("Error: another error occurred")
finally:
    print("Cleanup can go here")
