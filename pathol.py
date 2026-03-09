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
        "Masson Trichrome",
        "PAS Staining",
        "Ziehl-Neelsen",
        "Gram Staining",
        "Von Kossa"
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

# ===============================
# MT staining Protocol
# ===============================

elif menu == "Masson Trichrome":

    st.header("Masson Trichrome Staining")

    tab1, tab2 = st.tabs(["Protocol", "Recipes"])

    with tab1:

        st.subheader("Masson Trichrome Protocol")

        st.markdown("""
1. Deparaffinize in xylene  
2. Rehydrate through graded alcohol  
3. Bouin's solution – 1 hour at 56°C  
4. Wash in running water  
5. Weigert iron hematoxylin – 10 min  
6. Biebrich scarlet-acid fuchsin – 10 min  
7. Phosphomolybdic / phosphotungstic acid – 10 min  
8. Aniline blue – 5 min  
9. 1% acetic acid – 2 min  
10. Dehydrate in ethanol  
11. Clear in xylene  
12. Mount
""")

    with tab2:

        st.subheader("Biebrich Scarlet Solution")

        vol = st.number_input("Volume (mL)", key="masson1")

        if st.button("Calculate Biebrich Scarlet"):

            scarlet = 0.9 * vol / 100
            fuchsin = 0.1 * vol / 100

            st.write("Biebrich scarlet:", round(scarlet,2), "g")
            st.write("Acid fuchsin:", round(fuchsin,2), "g")
            st.write("Distilled water:", vol, "mL")

        st.subheader("Aniline Blue")

        vol2 = st.number_input("Volume (mL)", key="masson2")

        if st.button("Calculate Aniline Blue"):

            aniline = 2.5 * vol2 / 100

            st.write("Aniline blue:", round(aniline,2), "g")
            st.write("Distilled water:", vol2, "mL")

# ===============================
# PAS staining Protocol
# ===============================

elif menu == "PAS Staining":

    st.header("PAS Staining")

    tab1, tab2 = st.tabs(["Protocol", "Recipes"])

    with tab1:

        st.markdown("""
1. Deparaffinize and hydrate  
2. Periodic acid – 5–10 min  
3. Rinse distilled water  
4. Schiff reagent – 15 min  
5. Running water – 5 min  
6. Counterstain hematoxylin  
7. Dehydrate alcohol  
8. Xylene  
9. Mount
""")

    with tab2:

        st.subheader("Periodic Acid Solution")

        vol = st.number_input("Volume (mL)", key="pas1")

        if st.button("Calculate Periodic Acid"):

            acid = 1 * vol / 100

            st.write("Periodic acid:", round(acid,2), "g")
            st.write("Distilled water:", vol, "mL")

        st.subheader("Schiff Reagent")

        vol2 = st.number_input("Volume (mL)", key="pas2")

        if st.button("Calculate Schiff"):

            basic_fuchsin = 0.5 * vol2 / 100

            st.write("Basic fuchsin:", round(basic_fuchsin,2), "g")
            st.write("Distilled water:", vol2, "mL")

# ===============================
# ZN staining Protocol
# ===============================

elif menu == "Ziehl-Neelsen":

    st.header("Ziehl-Neelsen Staining")

    tab1, tab2 = st.tabs(["Protocol", "Recipes"])

    with tab1:

        st.markdown("""
1. Deparaffinize slide  
2. Flood with carbol fuchsin  
3. Heat gently until steaming  
4. Wash with water  
5. Decolorize with acid alcohol  
6. Wash water  
7. Counterstain methylene blue  
8. Wash and dry
""")

    with tab2:

        st.subheader("Carbol Fuchsin")

        vol = st.number_input("Volume (mL)", key="zn1")

        if st.button("Calculate Carbol Fuchsin"):

            fuchsin = 1 * vol / 100
            phenol = 5 * vol / 100

            st.write("Basic fuchsin:", round(fuchsin,2), "g")
            st.write("Phenol:", round(phenol,2), "g")
            st.write("Distilled water:", vol, "mL")

        st.subheader("Acid Alcohol")

        vol2 = st.number_input("Volume (mL)", key="zn2")

        if st.button("Calculate Acid Alcohol"):

            hcl = 1 * vol2 / 100
            ethanol = vol2

            st.write("HCl:", round(hcl,2), "mL")
            st.write("70% ethanol:", ethanol, "mL")

# ===============================
# Gram staining Protocol
# ===============================

elif menu == "Gram Staining":

    st.header("Gram Staining")

    tab1, tab2 = st.tabs(["Protocol", "Recipes"])

    with tab1:

        st.markdown("""
1. Crystal violet – 1 min  
2. Wash water  
3. Gram iodine – 1 min  
4. Decolorize alcohol  
5. Safranin – 30 sec  
6. Wash and dry
""")

    with tab2:

        st.subheader("Crystal Violet")

        vol = st.number_input("Volume (mL)", key="gram1")

        if st.button("Calculate Crystal Violet"):

            dye = 2 * vol / 100

            st.write("Crystal violet:", round(dye,2), "g")
            st.write("Distilled water:", vol, "mL")

        st.subheader("Safranin")

        vol2 = st.number_input("Volume (mL)", key="gram2")

        if st.button("Calculate Safranin"):

            dye = 0.5 * vol2 / 100

            st.write("Safranin:", round(dye,2), "g")
            st.write("Distilled water:", vol2, "mL")

# ===============================
# Gram staining Protocol
# ===============================

elif menu == "Von Kossa":

    st.header("Von Kossa Staining")

    tab1, tab2 = st.tabs(["Protocol", "Recipes"])

    with tab1:

        st.markdown("""
1. Deparaffinize  
2. Silver nitrate – 30–60 min under light  
3. Wash water  
4. Sodium thiosulfate – 5 min  
5. Counterstain nuclear fast red  
6. Dehydrate alcohol  
7. Clear xylene  
8. Mount
""")

    with tab2:

        st.subheader("Silver Nitrate")

        vol = st.number_input("Volume (mL)", key="vk1")

        if st.button("Calculate Silver Nitrate"):

            silver = 5 * vol / 100

            st.write("Silver nitrate:", round(silver,2), "g")
            st.write("Distilled water:", vol, "mL")

        st.subheader("Sodium Thiosulfate")

        vol2 = st.number_input("Volume (mL)", key="vk2")

        if st.button("Calculate Thiosulfate"):

            thio = 5 * vol2 / 100

            st.write("Sodium thiosulfate:", round(thio,2), "g")
            st.write("Distilled water:", vol2, "mL")
