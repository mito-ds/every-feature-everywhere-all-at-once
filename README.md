# Everything Bagel

> I got bored one day and put all of Mito's features in one demo

### What is this repo?
This repo is a central location for all of Mito's demos. It's purpose is to make it easy for users to find demos that are relevant to them.

Each demo has its own folder in the `Demos` folder. Inside each demo folder is a README.md file that gives context for who each demo is relevant to, instructions on how to conduct the demo, a Jupyter notebook configured for the demo, and all of the required data. In addition to the Jupyter notebook, each demo can be run through a Streamlit app. The README.md file will tell you which Streamlit app to use.

Note that we don't create a separate Streamlit app for each demo so we can easily upgrade the Streamlit apps without having to do so for each demo. This also gives you flexibility as the demoer to show off multiple demos without restarting your environment.

### What demos exist?
- [Data Ontology Verification](Demos/data-ontology-verification): Use Mito to verify that data conforms to a required schema. One scenario uses Mito open source features and another uses Mito enterprise features.
- [Vanguard Fund Performance](Demos/vanguard-fund-performance): Use Mito automate the creation of a formatted Excel file using Mito enterprise features. 


### How to run these demos locally?

1. Clone this repo
2. Create a virtual environment
```
python -m venv mito-demo
```
3. Activate the virtual environment (windows)
```
mito-demo\Scripts\activate.bat
```
4. Activate the virtual environment (mac)
```
source mito-demo/bin/activate
```
5. Install the requirements
```
pip install -r requirements.txt
```
6. Navigate to the demo you want to run in the [Demos](Demos) folder and follow the instructions in the README.md file