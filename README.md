# Robotic Arm Kinematics: FK & IK Solver

This project implements a **Forward Kinematics (FK)** and **Inverse Kinematics (IK)** solver in C++ for a 6-DOF robotic arm (Kinova Gen3). It uses the **Cyclic Coordinate Descent (CCD)** algorithm to solve the IK problem and generates Python scripts to visualize the robot's movement in **Blender**.

## 🎥 Demo
[Insert your video demo here]
## 🚀 Features

* [cite_start]**Forward Kinematics:** Calculates the global 3D position and orientation of the end-effector given a set of joint angles [cite: 242-245].
* [cite_start]**Inverse Kinematics (CCD):** Solves for the required joint angles to reach a specific target position $(x, y, z)$ and orientation $(r, p, y)$ using the iterative Cyclic Coordinate Descent algorithm [cite: 392-396].
* [cite_start]**Blender Integration:** Automatically generates a Python script (`my_script.py`) that animates the robot's solution in Blender.
* [cite_start]**Configurable Robot:** Loads robot configuration (links, joints, limits) from a `config.toml` file[cite: 318].

## 🛠️ Dependencies

[cite_start]The project relies on the following C++ libraries [cite: 551-554]:
* **[GLM](https://github.com/g-truc/glm):** For vector and matrix mathematics.
* **[fmt](https://github.com/fmtlib/fmt):** For safe and fast string formatting.
* **[toml++](https://github.com/marzer/tomlplusplus):** For parsing the robot configuration file.
* **CMake (3.22+):** Build system.
* **C++20 Compiler:** Required for modern C++ features.

## 📦 Installation & Build

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/TFelbor/CPP-Project2.git](https://github.com/TFelbor/CPP-Project2.git)
    cd CPP-Project2/source
    ```

2.  **Build using CMake:**
    ```bash
    mkdir build
    cd build
    cmake ..
    make
    ```
    *(On Windows, you may use `cmake --build .` or open the generated Visual Studio solution)*[cite: 846].

## 💻 Usage

Run the compiled executable `robot_kinematic.exe` (or `./ik.exe`) from the command line.

### 1. Forward Kinematics
Calculate the end-effector position for a specific set of joint angles (in degrees).
```bash
./robot_kinematic.exe --angles 0,0,0,0,0,0
```
