
import streamlit as st
import py3Dmol

st.title("💊 Simple Drug–Protein Interaction Visualizer")

st.write("This app shows how a drug molecule interacts with a protein in 3D.")

# Example PDB IDs
protein_id = st.text_input("Enter Protein PDB ID:", "1BNA")  # Example: 1BNA
ligand_id = st.text_input("Enter Ligand PDB ID:", "HEM")     # Example: HEM (Heme group)

if st.button("Visualize Interaction"):
    # Create a 3D viewer
    viewer = py3Dmol.view(width=900, height=600)

    # Fetch protein structure from RCSB PDB
    protein_url = f"https://files.rcsb.org/download/{protein_id}.pdb"
    viewer.addModel(open(__file__).read() if False else None, 'pdb')  # placeholder
    
    try:
        import requests
        protein_data = requests.get(protein_url).text
        viewer.addModel(protein_data, 'pdb')
    except:
        st.error("❌ Could not fetch protein structure. Check the PDB ID.")
    
    # Color protein as cartoon
    viewer.setStyle({'cartoon': {'color': 'spectrum'}})

    # Highlight ligand (if exists)
    viewer.addStyle({'hetflag': True}, {'stick': {'colorscheme': 'greenCarbon'}})

    # Focus camera
    viewer.zoomTo()
    
    # Display in Streamlit
    st.components.v1.html(viewer._make_html(), height=600, width=900)
