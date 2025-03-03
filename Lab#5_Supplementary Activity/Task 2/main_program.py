import projectilemotion

def main():
    velocity = float(input("Enter initial velocity (m/s): "))
    angle = float(input("Enter launch angle (degrees): "))

    range_distance, max_height = projectilemotion.projectilemotion_solver(velocity, angle)

    print(f"Horizontal Distance (Range): {range_distance:.2f} meters")
    print(f"Maximum Height: {max_height:.2f} meters")

    with open("output.txt", "w") as file:
        file.write(f"Velocity: {velocity} m/s\n")
        file.write(f"Angle: {angle} degrees\n")
        file.write(f"Range: {range_distance:.2f} meters\n")
        file.write(f"Max Height: {max_height:.2f} meters\n")

if __name__ == "__main__":
    main()
