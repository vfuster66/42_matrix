import sys
import os
import subprocess

EXERCISE_DIR = "."
TEST_DIR = "tests"


def list_exercises():
    print("Available exercises:")
    for folder in os.listdir():
        if folder.startswith("ex") and os.path.isdir(folder):
            print(f"- {folder}")


def run_exercise(ex_name):
    script_path = os.path.join(ex_name, f"{ex_name}.py")
    if os.path.exists(script_path):
        print(f"Running {script_path}...\n")
        subprocess.run(["python", script_path])
    else:
        print(f"Error: {script_path} not found.")


def run_tests(ex_name):
    test_path = os.path.join(TEST_DIR, f"{ex_name}.py")  # Ex: "tests/00.py"
    if os.path.exists(test_path):
        print(f"Running tests in {test_path}...\n")
        subprocess.run(["python", test_path])  # Exécute directement le fichier
    else:
        print(f"Error: {test_path} not found.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <exercise_folder> [--test]")
        list_exercises()
    else:
        exercise = sys.argv[1]
        if os.path.exists(exercise):
            run_exercise(exercise)
            if len(sys.argv) > 2 and sys.argv[2] == "--test":
                run_tests(exercise)
        else:
            print(f"Error: {exercise} not found.")
