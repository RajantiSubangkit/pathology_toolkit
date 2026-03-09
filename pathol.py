import streamlit as st

st.title("Bogor Vet. Pathol. Lab Toolkit")

st.sidebar.title("Calculator Menu")

menu = st.sidebar.radio(
    "Choose Tool",
    [
        "10% Neutral Buffered Formalin",
        "Alcohol Dilution",
        "Antibody Dilution (IHC)",
        "PBS Preparation",
        "H&E Staining",
    ]
)

# ===============================
# 10% Neutral Buffered Formalin
# ===============================

if menu == "10% Neutral Buffered Formalin":

    st.header("10% Neutral Buffered Formalin Calculator")

    volume = st.number_input(
        "Final volume (Liters)",
        min_value=0.1,
        key="nbf_volume"
    )

    if st.button("Calculate NBF"):

        formaldehyde = 100 * volume
        NaH2PO4 = 4 * volume
        Na2HPO4 = 6.5 * volume
        water = (1000 * volume) - formaldehyde

        st.subheader("Required Components")

        st.write("37–40% Formaldehyde:", round(formaldehyde,2), "mL")
        st.write("NaH2PO4:", round(NaH2PO4,2), "g")
        st.write("Na2HPO4:", round(Na2HPO4,2), "g")
        st.write("Distilled Water:", round(water,2), "mL")

# ===============================
# Alcohol Dilution
# ===============================

elif menu == "Alcohol Dilution":

    st.header("Alcohol Dilution Calculator")

    C1 = st.number_input("Stock concentration (%)", key="alc_c1")
    C2 = st.number_input("Final concentration (%)", key="alc_c2")
    V2 = st.number_input("Final volume (mL)", key="alc_v2")

    if st.button("Calculate Alcohol"):

        V1 = (C2 * V2) / C1
        water = V2 - V1

        st.subheader("Results")

        st.write("Stock alcohol:", round(V1,2), "mL")
        st.write("Distilled water:", round(water,2), "mL")

# ===============================
# Antibody Dilution
# ===============================

elif menu == "Antibody Dilution (IHC)":

    st.header("IHC Antibody Dilution Calculator")

    dilution = st.text_input(
        "Dilution ratio (example 1:200)",
        key="ab_ratio"
    )

    volume = st.number_input(
        "Final volume (µL)",
        key="ab_volume"
    )

    if st.button("Calculate Antibody"):

        try:

            ratio = int(dilution.split(":")[1])

            antibody = volume / ratio
            diluent = volume - antibody

            st.subheader("Results")

            st.write("Primary antibody:", round(antibody,2), "µL")
            st.write("Diluent:", round(diluent,2), "µL")

        except:

            st.error("Format must be like 1:200")

# ===============================
# PBS Calculator
# ===============================

elif menu == "PBS Preparation":

    st.header("PBS Preparation Calculator")

    volume = st.number_input(
        "Volume (Liters)",
        key="pbs_volume"
    )

    if st.button("Calculate PBS"):

        NaCl = 8 * volume
        KCl = 0.2 * volume
        Na2HPO4 = 1.44 * volume
        KH2PO4 = 0.24 * volume

        st.subheader("Required Components")

        st.write("NaCl:", round(NaCl,2), "g")
        st.write("KCl:", round(KCl,2), "g")
        st.write("Na2HPO4:", round(Na2HPO4,2), "g")
        st.write("KH2PO4:", round(KH2PO4,2), "g")
# ===============================
# H&E staining Protocol
# ===============================

elif menu == "H&E Staining":

    st.header("Hematoxylin & Eosin (H&E) Staining")

    tab1, tab2, tab3 = st.tabs(
        ["Protocol", "Hematoxylin Recipe", "Eosin Recipe"]
    )

    # -------------------------
    # Protocol
    # -------------------------

    with tab1:

        st.subheader("H&E Staining Protocol")

        st.markdown("""
### Deparaffinization
1. Xylene I – 5 min  
2. Xylene II – 5 min  

### Rehydration
3. Absolute ethanol – 3 min  
4. 95% ethanol – 3 min  
5. 70% ethanol – 3 min  
6. Running tap water – 2 min  

### Nuclear Staining
7. Hematoxylin – 5 min  
8. Running water – 5 min  

### Differentiation
9. Acid alcohol – few seconds  

### Bluing
10. Scott tap water – 1 min  

### Cytoplasmic Stain
11. Eosin – 1–2 min  

### Dehydration
12. 70% ethanol  
13. 95% ethanol  
14. Absolute ethanol  

### Clearing
15. Xylene  

### Mounting
16. Mounting medium + coverslip
""")

    # -------------------------
    # Hematoxylin
    # -------------------------

    with tab2:

        st.subheader("Harris Hematoxylin Recipe")

        volume = st.number_input(
            "Final volume (mL)",
            min_value=100.0,
            key="hema_vol"
        )

        if st.button("Calculate Hematoxylin"):

            hematoxylin = 5 * volume / 1000
            ethanol = 50 * volume / 1000
            alum = 100 * volume / 1000
            acetic = 40 * volume / 1000

            st.write("Hematoxylin:", round(hematoxylin,2), "g")
            st.write("Absolute ethanol:", round(ethanol,2), "mL")
            st.write("Ammonium/Potassium alum:", round(alum,2), "g")
            st.write("Glacial acetic acid:", round(acetic,2), "mL")
            st.write("Distilled water: up to", volume, "mL")

    # -------------------------
    # Eosin
    # -------------------------

    with tab3:

        st.subheader("Eosin Y Recipe")

        volume = st.number_input(
            "Final volume (mL)",
            min_value=100.0,
            key="eosin_vol"
        )

        if st.button("Calculate Eosin"):

            eosin = 1 * volume / 100
            alcohol = volume
            acetic = 0.5 * volume / 100

            st.write("Eosin Y:", round(eosin,2), "g")
            st.write("95% Ethanol:", round(alcohol,2), "mL")
            st.write("Glacial acetic acid:", round(acetic,2), "mL")
