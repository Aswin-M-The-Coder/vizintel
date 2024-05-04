import subprocess
import pandas as pd

# Define the command and input
command = "ollama run llama2"
input_data = "goal:"
user_data=input().strip()
input_data+=user_data
input_data+='''Give me the python code to generate single statiscal plot for above goal for data in the data.csv file and the output plot has to be saved in output directory as images.
# Your output should be in the following json format.
#also also plt.xlabel(), plt.ylabel(),plt.title()
# {code : <python code of your response>}
Don't use plt.show() in the code, use only plt.savefig() to save the plot as image in the directory named 'output'.
# pathe is plt.savefig('images/plot.png')
#depends upon data use plt.plot(), plt.bar(), plt.scatter() or any one which is suitable for goal
#also add plt.figure(figsize=(20, 10)) plt.xticks(rotation=90,fontsize=10) plt.tight_layout()
The sample data is,'''

df = pd.read_csv("data.csv")

first_10_rows = df.head(10)
columns = df.columns

formatted_data = ",".join(columns) + "\n"  # Add column names
formatted_data += "\n".join([",".join(map(str, row)) for row in first_10_rows.values])

input_data+=formatted_data

# Run the command
result = subprocess.run(command, input=input_data, shell=True, capture_output=True, text=True)

# Print the result
print("Command output:", result.stdout)


prompt2 = '''parse and give me only python code by removing unneccasary words and lines from thie follwing response:
"'''
prompt2+=result.stdout

prompt2+='''"

Your output should be in the following format.
# code:
# ```python
# <parsed python code>
# ```
'''

result = subprocess.run(command, input=prompt2, shell=True, capture_output=True, text=True)

# Print the result
print("Command output:", result.stdout)

start = result.stdout.find("```python")
if start == -1:
    start = result.stdout.find("```")
    start += 3
else:
    start += 9
end = result.stdout.find("```", start)

python_code = result.stdout[start:end]

with open("plot.py", "w") as file:
    file.write(python_code)


result_text = subprocess.run(command, input="goal:"+user_data+"general writing about the goal with data.csv", shell=True, capture_output=True, text=True)


with open("answer.txt", "w") as file:
    file.write(result_text.stdout)
