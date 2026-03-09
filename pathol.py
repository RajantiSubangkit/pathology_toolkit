import streamlit as st

st.title("Vet. Pathol. Lab Toolkit")

st.sidebar.title("Calculator Menu")

menu = st.sidebar.radio(
    "Choose Tool",
    [
        "10% Neutral Buffered Formalin",
        "Alcohol Dilution",
        "Immunohistochemistry",
        "PBS Preparation",
        "H&E Staining",
        "Masson Trichrome",
        "PAS Staining",
        "Ziehl-Neelsen",
        "Gram Staining",
        "Von Kossa",
        "Giemsa Staining",
        "Toluidine Blue",
        "Congo Red",
        "Prussian Blue",
        "Reticulin Stain",
        "Alcian Blue",
        "Oil Red O",
        "Sudan Black B",
        "Verhoeff Van Gieson",
        "Van Gieson",
        "Luxol Fast Blue",
        "Warthin Starry"
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
# IHC
# ===============================

elif menu == "Immunohistochemistry":

    st.header("Immunohistochemistry (IHC)")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Protocol",
        "Antibody Dilution",
        "Blocking Buffer",
        "Antigen Retrieval Buffer",
        "DAB Substrate"
    ])

# ==============================
# IHC PROTOCOL
# ==============================

    with tab1:

        st.markdown("""
### Deparaffinization
1. Xylene – 2 changes  
2. Absolute ethanol  
3. 95% ethanol  
4. 70% ethanol  
5. Distilled water  

### Antigen Retrieval
6. Heat in citrate buffer pH 6.0 or Tris-EDTA pH 9.0 (microwave / water bath)

### Blocking Endogenous Peroxidase
7. 3% H₂O₂ – 10 min  

### Blocking Non-specific Binding
8. Normal serum or BSA blocking buffer – 20 min  

### Primary Antibody
9. Incubate primary antibody – 1 hour or overnight  

### Secondary Antibody
10. HRP-conjugated secondary antibody – 30 min  

### Chromogen
11. DAB substrate – 3–10 min  

### Counterstain
12. Hematoxylin – 1 min  

### Dehydration
13. Alcohol series  
14. Xylene  

### Mount
15. Mounting medium
""")

# ==============================
# ANTIBODY DILUTION
# ==============================

    with tab2:

        st.subheader("Primary Antibody Dilution")

        dilution = st.text_input("Dilution ratio (example 1:200)")
        volume = st.number_input("Final volume (µL)", key="ihc_ab")

        if st.button("Calculate Antibody"):

            try:

                ratio = int(dilution.split(":")[1])

                antibody = volume / ratio
                diluent = volume - antibody

                st.write("Primary antibody:", round(antibody,2), "µL")
                st.write("Antibody diluent:", round(diluent,2), "µL")

            except:

                st.error("Format example: 1:200")

# ==============================
# BLOCKING BUFFER
# ==============================

    with tab3:

        st.subheader("Blocking Buffer (1% BSA in PBS)")

        vol = st.number_input("Volume (mL)", key="block")

        if st.button("Calculate Blocking Buffer"):

            bsa = vol * 1 / 100

            st.write("BSA:", round(bsa,2), "g")
            st.write("PBS:", vol, "mL")

# ==============================
# ANTIGEN RETRIEVAL BUFFER
# ==============================

    with tab4:

        st.subheader("Citrate Buffer pH 6.0")

        vol = st.number_input("Volume (mL)", key="citrate")

        if st.button("Calculate Citrate Buffer"):

            citrate = vol * 2.94 / 1000

            st.write("Citric acid:", round(citrate,3), "g")
            st.write("Distilled water:", vol, "mL")
            st.write("Adjust pH to 6.0 with NaOH")


        st.subheader("Tris-EDTA Buffer pH 9")

        vol2 = st.number_input("Volume (mL)", key="tris")

        if st.button("Calculate Tris Buffer"):

            tris = vol2 * 1.21 / 1000
            edta = vol2 * 0.37 / 1000

            st.write("Tris base:", round(tris,3), "g")
            st.write("EDTA:", round(edta,3), "g")
            st.write("Distilled water:", vol2, "mL")

# ==============================
# DAB SUBSTRATE
# ==============================

    with tab5:

        st.subheader("DAB Substrate Solution")

        vol = st.number_input("Volume (mL)", key="dab")

        if st.button("Calculate DAB"):

            dab = vol * 0.5 / 100
            h2o2 = vol * 0.03 / 100

            st.write("DAB:", round(dab,3), "g")
            st.write("H₂O₂:", round(h2o2,3), "mL")
            st.write("Tris buffer:", vol, "mL")

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

    tab1, tab2 = st.tabs(["Protocol", "Reagent Recipes"])

    # ===============================
    # PROTOCOL
    # ===============================

    with tab1:

        st.subheader("Masson Trichrome Protocol")

        st.markdown("""
### Deparaffinization
1. Xylene I – 5 min  
2. Xylene II – 5 min  

### Rehydration
3. Absolute ethanol – 2 min  
4. 95% ethanol – 2 min  
5. 70% ethanol – 2 min  
6. Distilled water  

### Mordant
7. Bouin solution – 1 hour at 56°C  

### Nuclear stain
8. Weigert Iron Hematoxylin – 10 min  

### Cytoplasmic stain
9. Biebrich Scarlet–Acid Fuchsin – 10 min  

### Differentiation
10. Phosphomolybdic / Phosphotungstic acid – 10 min  

### Collagen stain
11. Aniline Blue – 5 min  

### Final differentiation
12. 1% Acetic acid – 2 min  

### Dehydration
13. 95% ethanol  
14. Absolute ethanol  

### Clearing
15. Xylene  

### Mounting
16. Mount with resin
""")

    # ===============================
    # RECIPES
    # ===============================

    with tab2:

        st.subheader("Bouin Solution")

        vol = st.number_input("Volume (mL)", key="bouin")

        if st.button("Calculate Bouin"):

            picric = 75 * vol / 100
            formalin = 25 * vol / 100
            acetic = 5 * vol / 100

            st.write("Saturated picric acid:", round(picric,2), "mL")
            st.write("37% formaldehyde:", round(formalin,2), "mL")
            st.write("Glacial acetic acid:", round(acetic,2), "mL")


        st.subheader("Weigert Iron Hematoxylin")

        vol2 = st.number_input("Volume (mL)", key="weigert")

        if st.button("Calculate Weigert"):

            hematox = 1 * vol2 / 100
            ethanol = 50 * vol2 / 100

            st.write("Hematoxylin:", round(hematox,2), "g")
            st.write("Absolute ethanol:", round(ethanol,2), "mL")
            st.write("Ferric chloride solution: equal volume mix")


        st.subheader("Biebrich Scarlet – Acid Fuchsin")

        vol3 = st.number_input("Volume (mL)", key="scarlet")

        if st.button("Calculate Biebrich"):

            scarlet = 0.9 * vol3 / 100
            fuchsin = 0.1 * vol3 / 100

            st.write("Biebrich scarlet:", round(scarlet,2), "g")
            st.write("Acid fuchsin:", round(fuchsin,2), "g")
            st.write("Distilled water:", vol3, "mL")


        st.subheader("Phosphomolybdic / Phosphotungstic Acid")

        vol4 = st.number_input("Volume (mL)", key="pta")

        if st.button("Calculate PTA"):

            pta = 5 * vol4 / 100

            st.write("Phosphotungstic acid:", round(pta,2), "g")
            st.write("Distilled water:", vol4, "mL")


        st.subheader("Aniline Blue")

        vol5 = st.number_input("Volume (mL)", key="aniline")

        if st.button("Calculate Aniline"):

            aniline = 2.5 * vol5 / 100

            st.write("Aniline blue:", round(aniline,2), "g")
            st.write("Distilled water:", vol5, "mL")


        st.subheader("1% Acetic Acid")

        vol6 = st.number_input("Volume (mL)", key="acetic")

        if st.button("Calculate Acetic"):

            acetic = 1 * vol6 / 100

            st.write("Glacial acetic acid:", round(acetic,2), "mL")
            st.write("Distilled water:", vol6, "mL")
# ===============================
# PAS staining Protocol
# ===============================

elif menu == "PAS Staining":

    st.header("PAS Staining")

    tab1, tab2 = st.tabs(["Protocol", "Reagent Recipes"])

    with tab1:

        st.markdown("""
### Deparaffinization
1. Xylene – 2 changes  
2. Absolute ethanol  
3. 95% ethanol  
4. 70% ethanol  
5. Distilled water  

### Oxidation
6. 1% Periodic acid – 5–10 min  

### Wash
7. Distilled water  

### Schiff Reaction
8. Schiff reagent – 10–15 min  

### Wash
9. Running tap water – 5–10 min  

### Counterstain
10. Hematoxylin – 1 min  

### Dehydration
11. 95% ethanol  
12. Absolute ethanol  

### Clearing
13. Xylene  

### Mount
14. Resin mounting medium
""")

    with tab2:

        st.subheader("1% Periodic Acid")

        vol = st.number_input("Volume (mL)", key="pas1")

        if st.button("Calculate Periodic Acid"):

            acid = vol * 1 / 100

            st.write("Periodic acid:", round(acid,2), "g")
            st.write("Distilled water:", vol, "mL")


        st.subheader("Schiff Reagent")

        vol2 = st.number_input("Volume (mL)", key="pas2")

        if st.button("Calculate Schiff"):

            fuchsin = 0.5 * vol2 / 100
            bisulfite = 1 * vol2 / 100

            st.write("Basic fuchsin:", round(fuchsin,2), "g")
            st.write("Sodium metabisulfite:", round(bisulfite,2), "g")
            st.write("Distilled water:", vol2, "mL")

# ===============================
# ZN staining Protocol
# ===============================

elif menu == "Ziehl-Neelsen":

    st.header("Ziehl-Neelsen Staining")

    tab1, tab2 = st.tabs(["Protocol", "Reagent Recipes"])

    with tab1:

        st.markdown("""
### Staining
1. Flood slide with Carbol Fuchsin  
2. Heat until steaming for 5 min  

### Wash
3. Running water  

### Decolorization
4. Acid alcohol – 1 min  

### Wash
5. Water  

### Counterstain
6. Methylene blue – 1 min  

### Wash
7. Water  

### Dry and mount
""")

    with tab2:

        st.subheader("Carbol Fuchsin")

        vol = st.number_input("Volume (mL)", key="zn1")

        if st.button("Calculate Carbol Fuchsin"):

            fuchsin = vol * 1 / 100
            phenol = vol * 5 / 100
            ethanol = vol * 10 / 100

            st.write("Basic fuchsin:", round(fuchsin,2), "g")
            st.write("Phenol crystals:", round(phenol,2), "g")
            st.write("95% ethanol:", round(ethanol,2), "mL")
            st.write("Distilled water: up to", vol, "mL")


        st.subheader("Acid Alcohol")

        vol2 = st.number_input("Volume (mL)", key="zn2")

        if st.button("Calculate Acid Alcohol"):

            hcl = vol2 * 3 / 100

            st.write("HCl:", round(hcl,2), "mL")
            st.write("70% ethanol:", vol2, "mL")


        st.subheader("Methylene Blue")

        vol3 = st.number_input("Volume (mL)", key="zn3")

        if st.button("Calculate Methylene Blue"):

            dye = vol3 * 0.3 / 100

            st.write("Methylene blue:", round(dye,2), "g")
            st.write("Distilled water:", vol3, "mL")

# ===============================
# Gram staining Protocol
# ===============================

elif menu == "Gram Staining":

    st.header("Gram Staining")

    tab1, tab2 = st.tabs(["Protocol", "Reagent Recipes"])

    with tab1:

        st.markdown("""
### Staining
1. Crystal violet – 1 min  

### Mordant
2. Gram iodine – 1 min  

### Decolorization
3. Ethanol or acetone alcohol  

### Counterstain
4. Safranin – 30 sec  

### Wash
5. Water  
""")

    with tab2:

        st.subheader("Crystal Violet")

        vol = st.number_input("Volume (mL)", key="gram1")

        if st.button("Calculate Crystal Violet"):

            dye = vol * 2 / 100

            st.write("Crystal violet:", round(dye,2), "g")
            st.write("Distilled water:", vol, "mL")


        st.subheader("Gram Iodine")

        vol2 = st.number_input("Volume (mL)", key="gram2")

        if st.button("Calculate Gram Iodine"):

            iodine = vol2 * 1 / 100
            iodide = vol2 * 2 / 100

            st.write("Iodine:", round(iodine,2), "g")
            st.write("Potassium iodide:", round(iodide,2), "g")
            st.write("Distilled water:", vol2, "mL")


        st.subheader("Safranin")

        vol3 = st.number_input("Volume (mL)", key="gram3")

        if st.button("Calculate Safranin"):

            dye = vol3 * 0.5 / 100

            st.write("Safranin:", round(dye,2), "g")
            st.write("Distilled water:", vol3, "mL")
# ===============================
# Von Kossa staining Protocol
# ===============================

elif menu == "Von Kossa":

    st.header("Von Kossa Staining")

    tab1, tab2 = st.tabs(["Protocol", "Reagent Recipes"])

    with tab1:

        st.markdown("""
### Deparaffinization
1. Xylene  

### Rehydration
2. Graded alcohol  

### Silver reaction
3. 5% Silver nitrate – 30–60 min under light  

### Wash
4. Distilled water  

### Fix silver
5. Sodium thiosulfate – 5 min  

### Counterstain
6. Nuclear fast red  

### Dehydrate
7. Alcohol  

### Clear
8. Xylene  

### Mount
""")

    with tab2:

        st.subheader("Silver Nitrate Solution")

        vol = st.number_input("Volume (mL)", key="vk1")

        if st.button("Calculate Silver"):

            silver = vol * 5 / 100

            st.write("Silver nitrate:", round(silver,2), "g")
            st.write("Distilled water:", vol, "mL")


        st.subheader("Sodium Thiosulfate")

        vol2 = st.number_input("Volume (mL)", key="vk2")

        if st.button("Calculate Thiosulfate"):

            thio = vol2 * 5 / 100

            st.write("Sodium thiosulfate:", round(thio,2), "g")
            st.write("Distilled water:", vol2, "mL")
# ===============================
# Giemsa staining Protocol
# ===============================

elif menu == "Giemsa Staining":

    st.header("Giemsa Staining")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize in xylene  
2. Hydrate through graded alcohol  
3. Rinse distilled water  
4. Stain with Giemsa solution 20–30 min  
5. Wash with buffer pH 6.8  
6. Differentiate briefly in acetic acid water  
7. Dehydrate alcohol  
8. Clear xylene  
9. Mount
""")

    with tab2:

        st.subheader("Giemsa Solution")

        vol = st.number_input("Volume (mL)", key="giemsa1")

        if st.button("Calculate Giemsa"):

            giemsa = vol * 1 / 100

            st.write("Giemsa powder:", round(giemsa,2), "g")
            st.write("Methanol:", vol, "mL")

# ===============================
# TB staining Protocol
# ===============================
elif menu == "Toluidine Blue":

    st.header("Toluidine Blue Staining")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize slide  
2. Hydrate to distilled water  
3. Toluidine blue solution – 2–5 min  
4. Wash water  
5. Dehydrate quickly  
6. Clear xylene  
7. Mount
""")

    with tab2:

        st.subheader("Toluidine Blue Solution")

        vol = st.number_input("Volume (mL)", key="tb1")

        if st.button("Calculate Toluidine Blue"):

            dye = vol * 1 / 100

            st.write("Toluidine blue:", round(dye,2), "g")
            st.write("Distilled water:", vol, "mL")

# ===============================
# Congo Red staining Protocol
# ===============================

elif menu == "Congo Red":

    st.header("Congo Red Staining (Amyloid)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize slide  
2. Hydrate to distilled water  
3. Congo red stain – 20 min  
4. Differentiate in alkaline alcohol  
5. Counterstain hematoxylin  
6. Dehydrate alcohol  
7. Clear xylene  
8. Mount

Amyloid shows apple-green birefringence under polarized light
""")

    with tab2:

        st.subheader("Congo Red Solution")

        vol = st.number_input("Volume (mL)", key="cr1")

        if st.button("Calculate Congo Red"):

            dye = vol * 0.5 / 100

            st.write("Congo red:", round(dye,2), "g")
            st.write("80% ethanol:", vol, "mL")

# ===============================
# Prussian Blue staining Protocol
# ===============================

elif menu == "Prussian Blue":

    st.header("Prussian Blue Staining (Iron)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize slide  
2. Hydrate to distilled water  
3. Mix potassium ferrocyanide + HCl  
4. Incubate 20–30 min  
5. Wash distilled water  
6. Counterstain nuclear fast red  
7. Dehydrate alcohol  
8. Clear xylene  
9. Mount
""")

    with tab2:

        st.subheader("Potassium Ferrocyanide Solution")

        vol = st.number_input("Volume (mL)", key="pb1")

        if st.button("Calculate Ferrocyanide"):

            salt = vol * 2 / 100

            st.write("Potassium ferrocyanide:", round(salt,2), "g")
            st.write("Distilled water:", vol, "mL")


        st.subheader("Hydrochloric Acid Solution")

        vol2 = st.number_input("Volume (mL)", key="pb2")

        if st.button("Calculate HCl"):

            acid = vol2 * 2 / 100

            st.write("HCl:", round(acid,2), "mL")
            st.write("Distilled water:", vol2, "mL")

# ===============================
# Reticulin staining Protocol
# ===============================

elif menu == "Reticulin Stain":

    st.header("Reticulin Stain (Gomori)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize slide  
2. Oxidize with potassium permanganate  
3. Bleach with oxalic acid  
4. Sensitize with iron alum  
5. Silver impregnation  
6. Reduce with formalin  
7. Tone with gold chloride  
8. Fix with sodium thiosulfate  
9. Counterstain nuclear fast red
""")

    with tab2:

        st.subheader("Potassium Permanganate")

        vol = st.number_input("Volume (mL)", key="ret1")

        if st.button("Calculate Permanganate"):

            salt = vol * 1 / 100

            st.write("Potassium permanganate:", round(salt,2), "g")
            st.write("Distilled water:", vol, "mL")


        st.subheader("Oxalic Acid")

        vol2 = st.number_input("Volume (mL)", key="ret2")

        if st.button("Calculate Oxalic Acid"):

            acid = vol2 * 1 / 100

            st.write("Oxalic acid:", round(acid,2), "g")
            st.write("Distilled water:", vol2, "mL")

# ===============================
# AB staining Protocol
# ===============================

elif menu == "Alcian Blue":

    st.header("Alcian Blue Staining (Acid Mucin)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize slide
2. Hydrate to distilled water
3. Alcian blue solution pH 2.5 – 30 min
4. Wash in running water
5. Counterstain nuclear fast red
6. Dehydrate alcohol
7. Clear xylene
8. Mount
""")

    with tab2:

        st.subheader("Alcian Blue Solution")

        vol = st.number_input("Volume (mL)", key="ab1")

        if st.button("Calculate Alcian Blue"):

            dye = vol * 1 / 100

            st.write("Alcian blue:", round(dye,2), "g")
            st.write("3% acetic acid:", vol, "mL")
# ===============================
# Oil Red O staining Protocol
# ===============================

elif menu == "Oil Red O":

    st.header("Oil Red O Staining (Lipid)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Frozen section preparation
2. Fix in formalin
3. Rinse distilled water
4. Oil Red O solution – 10–15 min
5. Rinse 60% isopropanol
6. Wash distilled water
7. Counterstain hematoxylin
8. Mount aqueous medium
""")

    with tab2:

        st.subheader("Oil Red O Solution")

        vol = st.number_input("Volume (mL)", key="oil1")

        if st.button("Calculate Oil Red O"):

            dye = vol * 0.5 / 100

            st.write("Oil Red O:", round(dye,2), "g")
            st.write("Isopropanol:", vol, "mL")
# ===============================
# Sudan Black staining Protocol
# ===============================

elif menu == "Sudan Black B":

    st.header("Sudan Black B Staining (Lipid)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Prepare frozen section
2. Fix with formalin
3. Stain with Sudan Black B – 10 min
4. Differentiate in ethanol
5. Wash water
6. Counterstain nuclear fast red
7. Mount
""")

    with tab2:

        st.subheader("Sudan Black B Solution")

        vol = st.number_input("Volume (mL)", key="sudan1")

        if st.button("Calculate Sudan Black"):

            dye = vol * 0.7 / 100

            st.write("Sudan Black B:", round(dye,2), "g")
            st.write("70% ethanol:", vol, "mL")
# ===============================
# VVG staining Protocol
# ===============================

elif menu == "Verhoeff Van Gieson":

    st.header("Verhoeff–Van Gieson Stain (Elastic Fibers)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize slide
2. Stain with Verhoeff solution
3. Differentiate in ferric chloride
4. Sodium thiosulfate rinse
5. Counterstain Van Gieson solution
6. Dehydrate alcohol
7. Clear xylene
8. Mount
""")

    with tab2:

        st.subheader("Verhoeff Solution")

        vol = st.number_input("Volume (mL)", key="vvg1")

        if st.button("Calculate Verhoeff"):

            hematox = vol * 5 / 100
            ferric = vol * 10 / 100

            st.write("Hematoxylin:", round(hematox,2), "g")
            st.write("Ferric chloride:", round(ferric,2), "g")
            st.write("Distilled water:", vol, "mL")
# ===============================
# VG staining Protocol
# ===============================

elif menu == "Van Gieson":

    st.header("Van Gieson Staining (Collagen)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize slide
2. Hematoxylin nuclear stain
3. Wash water
4. Van Gieson solution – 2–5 min
5. Dehydrate alcohol
6. Clear xylene
7. Mount
""")

    with tab2:

        st.subheader("Van Gieson Solution")

        vol = st.number_input("Volume (mL)", key="vg1")

        if st.button("Calculate Van Gieson"):

            picric = vol * 90 / 100
            fuchsin = vol * 1 / 100

            st.write("Saturated picric acid:", round(picric,2), "mL")
            st.write("Acid fuchsin:", round(fuchsin,2), "g")
# ===============================
# Luxol staining Protocol
# ===============================

elif menu == "Luxol Fast Blue":

    st.header("Luxol Fast Blue Staining (Myelin)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize slide
2. Stain with Luxol Fast Blue overnight
3. Differentiate with lithium carbonate
4. Wash alcohol
5. Counterstain cresyl violet
6. Dehydrate alcohol
7. Clear xylene
8. Mount
""")

    with tab2:

        st.subheader("Luxol Fast Blue Solution")

        vol = st.number_input("Volume (mL)", key="lfb1")

        if st.button("Calculate LFB"):

            dye = vol * 0.1 / 100

            st.write("Luxol fast blue:", round(dye,3), "g")
            st.write("95% ethanol:", vol, "mL")
# ===============================
# Warthin Starry staining Protocol
# ===============================

elif menu == "Warthin Starry":

    st.header("Warthin–Starry Staining (Spirochetes)")

    tab1, tab2 = st.tabs(["Protocol","Reagent Recipes"])

    with tab1:

        st.markdown("""
### Protocol

1. Deparaffinize slide
2. Silver nitrate impregnation
3. Developer solution
4. Wash distilled water
5. Dehydrate alcohol
6. Clear xylene
7. Mount
""")

    with tab2:

        st.subheader("Silver Nitrate Solution")

        vol = st.number_input("Volume (mL)", key="ws1")

        if st.button("Calculate Silver"):

            silver = vol * 1 / 100

            st.write("Silver nitrate:", round(silver,2), "g")
            st.write("Distilled water:", vol, "mL")

st.sidebar.markdown("---")
st.sidebar.markdown(
"""
**Reference**

Developed by:  
Soleh, Kasnadi, Subangkit M. (2026)  
Veterinary Pathology Laboratory Toolkit
"""
)
