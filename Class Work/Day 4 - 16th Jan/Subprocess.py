import subprocess
result = subprocess.run(
    "echo" "Hello Rahul!",
    shell=True,
    capture_output=True,
    text=True
)
print(result.stdout)

subprocess.run(("python","ABC_Contructor.py"))