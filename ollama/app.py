import streamlit as st
import subprocess
import os
import pandas as pd

def execute_python_code(prompt):
    # Define the command to run the Main.py file
    command = "python test.py"
    # Convert the prompt to bytes using UTF-8 encoding
    input_data = prompt.encode('utf-8')
    # Run the command
    subprocess.run(command, input=input_data, shell=True)
    #run python file to generate plot
    command = "python plot.py"
    # Run the command
    subprocess.run(command, input=input_data, shell=True)


def main():
    #wide mode
    st.set_page_config(layout="wide")

    #Title
    st.title("Interact with CSV")

    # File uploader for CSV file
    csv_file = st.file_uploader("Upload CSV file", type=["csv"])
    if csv_file is not None:
        # Save uploaded CSV file locally as data.csv
        data_filename = "data.csv"
        data = pd.read_csv(csv_file)
        data.to_csv(data_filename, index=False)
        st.write(f"CSV file saved as {data_filename}")

        # Input prompt
        prompt = st.text_area("Enter your prompt")

        ind=0
        # Button to execute code
        if st.button("Generate plot"):
            execute_python_code(prompt)
            # Display output image
            image_path = "images/plot.png"
            if os.path.exists(image_path):
                st.image(image_path, caption="Output Image", use_column_width=True)
                ind+=1
            else:
                st.error("Output image not found.")
                ind+=1
                
            # Read and display solution from answer.txt file
            answer_file = "answer.txt"
            if os.path.exists(answer_file):
                with open(answer_file, "r") as file:
                    answer_text = file.read()
                    st.write(answer_text)
            else:
                st.error("Answer file not found.")

        # Button to Rewrite prompt
        if ind>0:
            if st.button("Rewrite prompt"):
                st.write("Edit your prompt")

if __name__ == "__main__":
    main()
